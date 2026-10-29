def attempt(operation, max_attempts):
    if type(max_attempts) is not int or max_attempts < 1:
        raise ValueError("max_attempts must be positive")
    for index in range(max_attempts):
        try:
            return operation()
        except TimeoutError:
            if index + 1 == max_attempts:
                raise
