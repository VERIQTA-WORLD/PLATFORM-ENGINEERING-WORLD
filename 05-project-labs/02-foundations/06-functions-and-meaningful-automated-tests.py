def required_cpu(replicas, per_replica):
    if type(replicas) is not int or replicas < 1:
        raise ValueError("replicas must be a positive integer")
    return replicas * per_replica
assert required_cpu(2, 0.5) == 1.0
assert required_cpu(4, 0.25) == 1.0
try:
    required_cpu(0, 0.5)
except ValueError:
    print("invalid input rejected")
else:
    raise AssertionError("zero replicas was accepted")
print("checks passed")
