#!/usr/bin/env python3
"""A local teaching platform. No network, credentials, or cloud resources."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import sys

NAME = re.compile(r"[a-z][a-z0-9-]{1,39}\Z")

def read(path):
    return json.loads(Path(path).read_text())

def violations(service):
    errors = []
    if not isinstance(service.get('name'), str) or not NAME.fullmatch(service['name']):
        errors.append('name must be 2–40 lowercase letters, digits or hyphens, starting with a letter')
    for key in ('owner', 'runbook'):
        if not isinstance(service.get(key), str) or not service[key].strip():
            errors.append(key + ' is required')
    if service.get('tier') not in ('critical', 'standard', 'experimental'):
        errors.append('tier must be critical, standard or experimental')
    replicas = service.get('replicas')
    if type(replicas) is not int or replicas < 1:
        errors.append('replicas must be an integer of at least 1')
    for key in ('public', 'auth'):
        if key in service and type(service[key]) is not bool:
            errors.append(key + ' must be a boolean')
    if service.get('public', False) and not service.get('auth', False):
        errors.append('public services require authentication')
    return errors

def validate(catalog):
    if not isinstance(catalog, dict) or not isinstance(catalog.get('services'), list):
        raise ValueError('catalog must contain a services list')
    errors, names = [], set()
    for service in catalog['services']:
        if not isinstance(service, dict):
            errors.append('each service must be an object')
            continue
        name = str(service.get('name', '?'))
        errors.extend(name + ': ' + e for e in violations(service))
        if name in names:
            errors.append(name + ': duplicate service')
        names.add(name)
    return errors

def reconcile(desired, actual):
    """Return a deterministic plan; removal requires a separate explicit action."""
    before = {s['name']: s for s in actual['services']}
    after = {s['name']: s for s in desired['services']}
    plan = []
    for name in sorted(after):
        if name not in before:
            plan.append({'action': 'create', 'name': name})
        elif after[name] != before[name]:
            plan.append({'action': 'update', 'name': name})
    for name in sorted(before.keys() - after.keys()):
        plan.append({'action': 'retain-unmanaged', 'name': name})
    return plan

def apply(desired, actual):
    errors = validate(desired)
    if errors:
        raise ValueError('; '.join(errors))
    merged = {s['name']: s for s in actual['services']}
    merged.update({s['name']: s for s in desired['services']})
    return {'services': [merged[k] for k in sorted(merged)]}

def reliability(events, target):
    if not 0 < target < 1:
        raise ValueError('target must be greater than 0 and less than 1')
    if not isinstance(events, list):
        raise ValueError('events must be a list')
    for event in events:
        if not isinstance(event, dict):
            raise ValueError('each event must be an object')
        status, latency = event.get('status'), event.get('latency_ms')
        if type(status) is not int or not 100 <= status <= 599:
            raise ValueError('status must be an integer from 100 to 599')
        if type(latency) not in (int, float) or not math.isfinite(latency) or latency < 0:
            raise ValueError('latency_ms must be a finite nonnegative number')
    total = len(events)
    if total == 0:
        raise ValueError('no events: availability is unknown')
    good = sum(e['status'] < 500 and e['latency_ms'] <= 300 for e in events)
    bad = total - good
    allowed = total * (1-target)
    return {'total': total, 'good': good, 'bad': bad,
            'availability': good/total, 'allowed_bad': round(allowed, 6),
            'remaining_budget': round(allowed-bad, 6),
            'burn_rate': round((bad/total)/(1-target), 6)}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for cmd in ('validate', 'plan', 'apply'):
        p = sub.add_parser(cmd)
        p.add_argument('desired')
        if cmd != 'validate': p.add_argument('actual')
        if cmd == 'apply': p.add_argument('--out', required=True)
    p = sub.add_parser('slo'); p.add_argument('events'); p.add_argument('--target', type=float, default=.99)
    p = sub.add_parser('cost'); p.add_argument('usage')
    p = sub.add_parser('scaffold'); p.add_argument('name'); p.add_argument('--owner', required=True); p.add_argument('--out', required=True)
    p = sub.add_parser('backup'); p.add_argument('source'); p.add_argument('--out', required=True)
    p = sub.add_parser('restore'); p.add_argument('backup'); p.add_argument('--out', required=True)
    args = parser.parse_args()
    if args.command == 'validate':
        errors = validate(read(args.desired))
        print(json.dumps({'valid': not errors, 'errors': errors}, indent=2))
        return 1 if errors else 0
    if args.command in ('plan', 'apply'):
        desired, actual = read(args.desired), read(args.actual)
        errors = validate(desired)
        if errors: raise ValueError('; '.join(errors))
        if args.command == 'plan': print(json.dumps(reconcile(desired, actual), indent=2))
        else: Path(args.out).write_text(json.dumps(apply(desired, actual), indent=2)+'\n')
    elif args.command == 'slo': print(json.dumps(reliability(read(args.events), args.target), indent=2))
    elif args.command == 'cost':
        usage = read(args.usage)
        totals = {}
        for item in usage:
            if not isinstance(item['owner'], str) or not item['owner'].strip():
                raise ValueError('usage owner is required')
            for key in ('hours', 'hourly_rate'):
                value = item[key]
                if type(value) not in (int, float) or not math.isfinite(value) or value < 0:
                    raise ValueError(key + ' must be a finite nonnegative number')
            totals[item['owner']] = totals.get(item['owner'], 0) + item['hours']*item['hourly_rate']
        print(json.dumps({k: round(v, 2) for k,v in sorted(totals.items())}, indent=2))
    elif args.command == 'scaffold':
        if not NAME.fullmatch(args.name): raise ValueError('invalid service name')
        if not args.owner.strip(): raise ValueError('owner is required')
        target = Path(args.out)
        target.mkdir(parents=True, exist_ok=False)
        service = {'name': args.name, 'owner': args.owner, 'tier': 'standard', 'replicas': 1,
                   'runbook': '01-docs/01-runbook.md', 'public': False, 'auth': True}
        (target/'01-service.json').write_text(json.dumps({'services': [service]}, indent=2)+'\n')
        (target/'01-docs').mkdir()
        (target/'01-docs'/'01-runbook.md').write_text('# '+args.name+' runbook\n\nOwner: '+args.owner+'\n\n## Diagnose\nValidate the service contract and inspect the deployment plan.\n\n## Recover\nRestore the last reviewed desired state and reconcile.\n')
    elif args.command == 'backup':
        payload = Path(args.source).read_text()
        envelope = {'payload': payload, 'sha256': hashlib.sha256(payload.encode()).hexdigest()}
        with Path(args.out).open('x') as f: json.dump(envelope, f, indent=2)
    elif args.command == 'restore':
        envelope = read(args.backup)
        if hashlib.sha256(envelope['payload'].encode()).hexdigest() != envelope['sha256']:
            raise ValueError('backup checksum mismatch')
        json.loads(envelope['payload'])
        with Path(args.out).open('x') as f: f.write(envelope['payload'])
    return 0

if __name__ == '__main__':
    try: sys.exit(main())
    except (ValueError, KeyError, TypeError, OSError) as exc:
        print('error: '+str(exc), file=sys.stderr)
        sys.exit(2)
