def factorial(n):
    if not hasattr(factorial, 'mem'):
        factorial.mem = {1: 1}
    if not n in factorial.mem:
        factorial.mem[n] = n * factorial(n - 1)
    return factorial.mem[n]
