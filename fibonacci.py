def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def strict_fibonacci(n):
    if type(n) is not int or n < 0:
        raise Exception('fibonacci argument should be a positive integer')
    return fibonacci(n)
