MIN_MERGE = 32 
 
def calc_min_run(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r

def insertion_sort(array, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and array[j] < array[j - 1]:
            temp = array[j]
            array[j] = array[j-1]
            array[j-1] = temp
            j -= 1
 
def merge(array, l, m, r):
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(array[l + i])
    for i in range(0, len2):
        right.append(array[m + 1 + i])
 
    i, j, k = 0, 0, l

    while i < len1 and j < len2:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
 
        else:
            array[k] = right[j]
            j += 1
 
        k += 1
 
    while i < len1:
        array[k] = left[i]
        k += 1
        i += 1

    while j < len2:
        array[k] = right[j]
        k += 1
        j += 1
 

def tim_sort(array):
    n = len(array)
    minRun = calc_min_run(n)

    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        insertion_sort(array, start, end)

    size = minRun
    while size < n:

        for left in range(0, n, 2 * size):

            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))

            if mid < right:
                merge(array, left, mid, right)
 
        size = 2 * size
    return array