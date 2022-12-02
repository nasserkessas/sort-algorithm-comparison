#include <cmath>

#include "sort.h"

void heapify(int *array, int len, int index) {
    int largest = index;
    int l = 2 * index + 1;
    int r = 2 * index + 2;
    if (l < len && array[largest] < array[l]) {
        largest = l;
    }
    if (r < len and array[largest] < array[r]) {
        largest = r;
    }
    if (largest != index) {
        int temp = array[index];
        array[index] = array[largest];
        array[largest] = temp;
        heapify(array, len, largest);
    }
}
 
void heap_sort(int *array, int len) {
 
    for (int i = floor(len/2) - 1; i > -1; i--) {
        heapify(array, len, i);
    }
 
    for (int i = len-1; i > 0; i--) {
        int temp = array[i];
        array[i] = array[0];
        array[0] = temp;
        heapify(array, i, 0);
    }
}