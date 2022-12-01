"""
Factorial using recursion
"""
def factorial(n):
    if type(n) != int:
        raise  TypeError('Number should be an integer type')
    elif n < 0:
        raise ValueError('Number should be greater than 0')
    else:
        if n == 0:
            result = 1
        elif n == 1:
            result = 1
        elif n > 1:
            result = n*factorial(n-1)
        return result