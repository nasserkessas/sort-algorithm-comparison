from random import shuffle

def merge_sort(array):
    if len(array) > 1:
        i = j = k = 0

        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]
        merge_sort(L)
        merge_sort(R)
 
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

    return array