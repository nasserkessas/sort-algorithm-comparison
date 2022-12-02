#include "sort.h"

void insertion_sort(int *array, int len) {
    for (int i = 1; i < len; i++) {
        int key = array[i];
        int j = i-1;
        while (j >= 0 and key < array[j]) {
            array[j + 1] = array[j];
            j -= 1;
        }
        array[j + 1] = key;
    }
}