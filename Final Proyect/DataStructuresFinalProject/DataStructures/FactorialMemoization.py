"""
Factorial using Memoization
"""
def factorial(n):
    cache = {}
    def factorial_Memoization(n):
        if type(n) != int:
            raise TypeError('Number should be an integer type')
        elif n < 0:
            raise ValueError('Number should be greater than 0')
        else:
            if n in cache.keys():
                return cache[n]
            if n == 0:
                result = 1
            elif n == 1:
                result = 1
            else:
                result = n * factorial(n - 1)
                cache[n] = result
            return result
    return factorial_Memoization(n)
