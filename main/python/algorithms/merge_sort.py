def merge_sort(array):
    n = len(array)
    if n > 1:
        i = j = k = 0

        mid = n//2
        L = array[:mid]
        R = array[mid:]
        merge_sort(L)
        merge_sort(R)

        nL = len(L)
        nR = len(R)
 
        while i < nL and j < nR:
            if L[i] <= R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
 
        while i < nL:
            array[k] = L[i]
            i += 1
            k += 1
 
        while j < nR:
            array[k] = R[j]
            j += 1
            k += 1

    return array