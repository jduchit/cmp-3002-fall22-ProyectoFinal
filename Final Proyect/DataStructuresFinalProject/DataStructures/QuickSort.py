"""
Quick Sort is a sorting algorithm that is based on the Divide and Conquer paradigm
"""
def quick_sort(array):
    if len(array) == 0:
        raise ValueError('array is empty')
    elif len(array) ==1:
        ordered_array = array
    else:
        pivot = array[0]
        # Initialize 3 arrays for greater, lesser and equal elements
        greater = []
        less = []
        equal = []
        for i in array:
            if i > pivot:
                greater.append(i)
            elif i < pivot:
                less.append(i)
            else:
                equal.append(i)
        ordered_array = quick_sort(less)+equal+quick_sort(greater)
    return ordered_array