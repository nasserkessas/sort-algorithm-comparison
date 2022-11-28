from random import shuffle

from bubble_sort import bubble_sort
from comb_sort import comb_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from radix_sort import radix_sort
from selection_sort import selection_sort

algorithms = [bubble_sort, comb_sort, insertion_sort, merge_sort, radix_sort, selection_sort]

ARRAY_LENGTH = 100

for algorithm in algorithms:
    array = []

    for n in range(ARRAY_LENGTH):
        array.append(n+1)

    shuffle(array)

    sorted = algorithm(array)