services = [
    {"name": "checkout", "owner": "commerce"},
    {"name": "search", "owner": ""},
]
missing = []
for service in services:
    if not service["owner"]:
        missing.append(service["name"])
print("services", len(services))
print("missing owners", missing)
