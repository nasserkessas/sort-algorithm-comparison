from random import shuffle

ARRAY_LENGTH = 100

def bubble_sort(array):
    for i in range(ARRAY_LENGTH):
        for j in range(0, ARRAY_LENGTH-i-1):
             if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
 
array = []

for n in range(ARRAY_LENGTH):
    array.append(n+1)

shuffle(array)

bubble_sort(array)