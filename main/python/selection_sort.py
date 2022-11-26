from random import shuffle

ARRAY_LENGTH = 100

def selection_sort(array):
    for i in range(ARRAY_LENGTH):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        temp = array[i]
        array[i] = array[min_idx]
        array[min_idx] = temp

array = []

for n in range(ARRAY_LENGTH):
    array.append(n+1)

shuffle(array)

selection_sort(array)