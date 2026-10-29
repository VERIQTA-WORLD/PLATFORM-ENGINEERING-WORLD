service = "checkout"
replicas = 2
cpu_per_replica = 0.5
public = False
print(service)
print(replicas * cpu_per_replica)
print(type(replicas).__name__)
print("2" * 3)
print(public)
