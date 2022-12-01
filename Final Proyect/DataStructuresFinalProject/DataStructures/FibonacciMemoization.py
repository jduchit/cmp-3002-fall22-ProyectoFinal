"""
Fibonacci using memoization
"""
def fibonacci(n):
    # cache implemented as dictionary
    cache = {}
    def fibonacci_Memoization(n):
        if type(n) != int:
            raise TypeError('Number should be an integer type')
        elif n < 0:
            raise ValueError('Number should be greater than 0')
        else:
            if n in cache.keys():
                return cache[n]
            if n == 0:
                res = 0
            elif n == 1:
                res = 1
            else:
                res = fibonacci_Memoization(n - 1) + fibonacci_Memoization(n - 2)
            cache[n] = res
            return res
    return fibonacci_Memoization(n)