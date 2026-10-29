def allowed(actor, action, target_tenant):
    permissions = {
        "reader": {"read"},
        "developer": {"read", "create"},
        "operator": {"read", "create", "update", "delete"},
    }
    return (actor.get("tenant") == target_tenant
            and action in permissions.get(actor.get("role"), set()))
