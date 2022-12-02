def comb_sort(array):
    n = len(array)
    gap = n
    swapped = True
    while gap !=1 or swapped == False:
        gap = (gap * 10)//13
        if gap < 1: gap = 1

        swapped = False
        for i in range(0, n-gap):
            if array[i] > array[i + gap]:
                temp = array[i]
                array[i] = array[i + gap]
                array[i + gap] = temp
                swapped = True
    
    return array