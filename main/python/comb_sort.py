def comb_sort(array):
    gap = len(array)
    swapped = True
    while gap !=1 or swapped == 1:
        gap = (gap * 10)//13
        if gap < 1: gap = 1

        swapped = False
        for i in range(0, len(array)-gap):
            if array[i] > array[i + gap]:
                temp = array[i]
                array[i]=array[i + gap]
                array[i + gap] = temp
                swapped = True
    
    return array