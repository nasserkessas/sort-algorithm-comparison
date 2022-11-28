from random import shuffle

ARRAY_LENGTH = 100

def comb_sort(array):
    gap = ARRAY_LENGTH
    swapped = True
    while gap !=1 or swapped == 1:
        gap = (gap * 10)//13
        if gap < 1: gap = 1

        swapped = False
        for i in range(0, ARRAY_LENGTH-gap):
            if array[i] > array[i + gap]:
                temp = array[i]
                array[i]=array[i + gap]
                array[i + gap] = temp
                swapped = True

array = []

for n in range(ARRAY_LENGTH):
    array.append(n+1)

shuffle(array)

comb_sort(array)