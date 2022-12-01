"""
Merge sort is a sorting algorithm that is based on the Divide and Conquer paradigm
"""
import string
def merge_sort(array):
    if len(array) == 0:
        raise ValueError('array is empty')
    else:
        if len(array) == 1:
            return array
        pivot = int(len(array) / 2)
        left = merge_sort(array[0:pivot])
        right = merge_sort(array[pivot:])
        return merge(left, right)

def merge(left, right):
    left_pointer = 0
    right_pointer = 0
    sorted_array = []
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            sorted_array.append(left[left_pointer])
            left_pointer += 1
        else:
            sorted_array.append(right[right_pointer])
            right_pointer += 1

    sorted_array.extend(left[left_pointer:])
    sorted_array.extend(right[right_pointer:])

    return sorted_array