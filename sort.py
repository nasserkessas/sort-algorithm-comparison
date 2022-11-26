from random import shuffle

ARR_LEN = 100

def bubbleSort(array):
    for i in range(ARR_LEN):
        for j in range(0, ARR_LEN-i-1):
             if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
 
array = []

for n in range(ARR_LEN):
    array.append(n+1)

shuffle(array)

bubbleSort(array)