# Counting sort cannot be used alone for numbers greater than 10

def counting_sort(array, digitIndex=1):
    n = len(array)

    output = [0] * n
 
    count = [0] * 10
 
    for i in range(0, n):
        digit = array[i] // digitIndex
        count[digit % 10] += 1
 
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    i = n - 1
    while i >= 0:
        digit = array[i] // digitIndex
        output[count[digit % 10] - 1] = array[i]
        count[digit % 10] -= 1
        i -= 1
 
    i = 0
    for i in range(0, n):
        array[i] = output[i]
    
    return array


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