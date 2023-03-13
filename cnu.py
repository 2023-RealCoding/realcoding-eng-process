def fibonacci(n: int) -> int:
    # Base case
    if n == 0:
        return 0
    if n < 2:
        return 1
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)
