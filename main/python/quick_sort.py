def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            temp = array[i]
            array[i] = array[pivot]
            array[pivot] = temp
    temp = array[pivot]
    array[pivot] = array[begin]
    array[begin] = temp
    return pivot

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    def _quick_sort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quick_sort(array, begin, pivot-1)
        _quick_sort(array, pivot+1, end)
        return array
    return _quick_sort(array, begin, end)