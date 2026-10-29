def validate(catalog):
    errors = []
    seen = set()
    for service in catalog["services"]:
        name = service.get("name")
        if not isinstance(name, str) or not name.strip():
            errors.append("name required")
        elif name in seen:
            errors.append("duplicate name")
        else:
            seen.add(name)
        if not isinstance(service.get("owner"), str) or not service["owner"].strip():
            errors.append("owner required")
        replicas = service.get("replicas")
        if type(replicas) is not int or replicas < 1:
            errors.append("invalid replicas")
    return errors
