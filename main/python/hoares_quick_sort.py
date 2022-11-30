def hoares_quick_sort(array):
    def _quicksort(array, low, high):
        # must run partition on sections with 2 elements or more
        if low < high: 
            p = partition(array, low, high)
            _quicksort(array, low, p)
            _quicksort(array, p+1, high)
    def partition(array, low, high):
        pivot = array[low]
        while True:
            while array[low] < pivot:
                low += 1
            while array[high] > pivot:
                high -= 1
            if low >= high:
                return high
            array[low], array[high] = array[high], array[low]
            low += 1
            high -= 1
    _quicksort(array, 0, len(array)-1)
    return array