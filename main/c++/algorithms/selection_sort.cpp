#include "sort.h"

void selection_sort(int *array, int len) {
    for (int i = 0; i < len; i++) {
        int min_idx = i;
        for (int j = i+1; j < len; j++) {
            if (array[min_idx] > array[j]) {
                min_idx = j;
            }
        }
        int temp = array[i];
        array[i] = array[min_idx];
        array[min_idx] = temp;
    }
}