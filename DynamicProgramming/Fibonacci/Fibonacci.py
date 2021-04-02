def fibonacci_recursive_non_memoized(n):
    assert n >= 1

    if n <= 2:
        return 1

    return fibonacci_recursive_non_memoized(n - 2) + fibonacci_recursive_non_memoized(n - 1)


cache = {}
def fibonacci_recursive_memoized(n):
    assert n >= 1

    if n <= 2:
        return 1

    if n not in cache:
        cache[n] = fibonacci_recursive_memoized(n - 2) + fibonacci_recursive_memoized(n - 1)

    return cache[n]


def fibonacci_dp(n):
    assert n >= 1

    if n <= 2:
        return 1

    previous = 1
    current = 1
    next = None

    for _ in range(3, n + 1):
        next = previous + current

        previous = current
        current = next

    return next
