def sum(n):
    '''Sum of the first n numbers'''
    if type(n) != int:
        raise TypeError('Int only !')
    elif n < 0:
        raise ValueError('Number should be greater than 0')
    else:
        total = 0
        for i in range(1, n+1):
            total += i
        return total
