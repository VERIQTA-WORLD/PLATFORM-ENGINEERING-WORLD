def plan(desired, actual):
    actions = []
    for name in sorted(desired):
        if name not in actual:
            actions.append(("create", name, desired[name]))
        elif desired[name] != actual[name]:
            actions.append(("update", name, desired[name]))
    for name in sorted(actual.keys() - desired.keys()):
        actions.append(("retain", name, actual[name]))
    return actions
