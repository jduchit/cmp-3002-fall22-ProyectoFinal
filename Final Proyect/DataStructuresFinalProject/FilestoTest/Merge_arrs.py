def merge_sorted_arrays(arr1, arr2):
    i=0
    j=0
    sorted_array =[]

    while ((i<len(arr1)) and (j<len(arr2))):
        if (arr1[i] < arr2[j]):
            sorted_array.append(arr1[i])
            i+=1
        else:
            sorted_array.append(arr2[j])
            j+=1
    while (i<len(arr1)):
        sorted_array.append(arr1[i])
        i+=1
    while (j < len(arr2)):
        sorted_array.append(arr2[j])
        j += 1
    return sorted_array