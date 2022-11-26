from random import shuffle

ARRAY_LENGTH = 100

def insertion_sort(array):
 
    for i in range(1, ARRAY_LENGTH):
 
        key = array[i]
 
        j = i-1
        while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
        array[j + 1] = key

array = []

for n in range(ARRAY_LENGTH):
    array.append(n+1)

shuffle(array)

insertion_sort(array)