"""
Fibonacci using recursion
"""
def fibonacci(n):
    if type(n) != int:
        raise  TypeError('Number should be an integer type')
    elif n < 0:
        raise ValueError('Number should be greater than 0')
    else:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
