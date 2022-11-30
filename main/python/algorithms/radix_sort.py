from counting_sort import counting_sort

def radix_sort(array):
    max = array[1]
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]

    index = 1
    while max / index >= 1:
        array = counting_sort(array, index)
        index *= 10
    
    return array