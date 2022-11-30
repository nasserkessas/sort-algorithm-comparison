from random import shuffle

from datetime import datetime

from bubble_sort import bubble_sort
from comb_sort import comb_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from radix_sort import radix_sort
from selection_sort import selection_sort
from quick_sort import quick_sort
from hoares_quick_sort import hoares_quick_sort
from tim_sort import tim_sort

algorithms = [bubble_sort, comb_sort, insertion_sort, merge_sort, radix_sort, selection_sort, quick_sort, hoares_quick_sort, tim_sort]
max_name_length = (len(max(map(lambda a: a.__name__, algorithms), key=len)))

ARRAY_LENGTH = 100
TRIALS = 2000

data = {}

for t in range(TRIALS):
    array = []

    for n in range(ARRAY_LENGTH):
        array.append(n+1)

    shuffle(array)

    for algorithm in algorithms:
        if algorithm.__name__ not in data:
            data[algorithm.__name__] = []
        thisArray = [*array]
        start = datetime.now()
        sorted = algorithm(thisArray)
        end = datetime.now()

        data[algorithm.__name__].append((end - start).total_seconds() * 10**3)

print(f"Average time to sort an array of {ARRAY_LENGTH} shuffled sequential numbers (tested {TRIALS} times):")
for a in data:
    print(f"{a.replace('_', ' ').capitalize()} {' ' * (max_name_length-len(a))} {(sum(data[a])/len(data[a])):.3f}ms")