def insertion_sort(array):
    '''Sort an array by insertion sort method'''
    arr = array.copy()
    for i in range(1, len(arr)):        
        key = arr[i]
        j = i-1
        while (j >= 0) and (key < arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr