def update(connection, name, expected_revision, replicas):
    if type(replicas) is not int or replicas < 1:
        raise ValueError("invalid replicas")
    with connection:
        cursor = connection.execute(
            "UPDATE services SET replicas=?, revision=revision+1 WHERE name=? AND revision=?",
            (replicas, name, expected_revision))
        if cursor.rowcount != 1:
            raise ValueError("stale or missing resource")
    return expected_revision + 1
