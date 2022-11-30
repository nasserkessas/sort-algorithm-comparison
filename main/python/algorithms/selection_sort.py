def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if array[min_idx] > array[j]:
                min_idx = j
        temp = array[i]
        array[i] = array[min_idx]
        array[min_idx] = temp

    return array