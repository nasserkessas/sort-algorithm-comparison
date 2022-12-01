import json
import os
from progress.bar import Bar
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
from heap_sort import heap_sort

algorithms = [bubble_sort, comb_sort, insertion_sort, merge_sort, radix_sort, selection_sort, quick_sort, hoares_quick_sort, tim_sort, heap_sort]
# algorithms = [comb_sort, merge_sort, radix_sort, quick_sort, hoares_quick_sort, tim_sort, heap_sort] # removed slow algorithms for better graph
max_name_length = (len(max(map(lambda a: a.__name__, algorithms), key=len)))

ARRAY_LENGTH_START = 50
ARRAY_LENGTH_INCREMENT = 50
ARRAY_LENGTH_END = 500
TRIALS = 5000

data = {}

file = open(os.path.join(os.path.dirname(__file__), 'data.json'), "w")

max_array_length_name = len(str(ARRAY_LENGTH_END))

for length in range(ARRAY_LENGTH_START, ARRAY_LENGTH_END+1, ARRAY_LENGTH_INCREMENT):
    data[length] = {}
    bar = Bar(f'Sorting with {length} items{" " * (max_array_length_name - int(len(str(length))))}', max=TRIALS, suffix="%(index)d/%(max)d [%(percent).1f%%] in %(elapsed)ds (eta: %(eta)ds)")
    for t in range(TRIALS):
        array = []

        for n in range(length):
            array.append(n+1)

        shuffle(array)

        for algorithm in algorithms:
            if algorithm.__name__.replace('_', ' ') not in data[length]:
                data[length][algorithm.__name__.replace('_', ' ')] = []
            thisArray = [*array]
            start = datetime.now()
            sorted = algorithm(thisArray)
            end = datetime.now()

            data[length][algorithm.__name__.replace('_', ' ')].append((end - start).total_seconds() * 10**3)
        bar.next()
    bar.finish()

for l in data:
    for f in data[l]:
        data[l][f] = list(map(lambda x: round(x,3), data[l][f]))

try:
    json.dump(data, file)
    file.close()
    print(f"\nSaved data to {os.path.join(os.path.dirname(__file__), 'data.json')}")
except:
    print(f"\nData could not be saved to {os.path.join(os.path.dirname(__file__), 'data.json')}")