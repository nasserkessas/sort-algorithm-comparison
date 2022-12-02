#include "sort.h"

void bubble_sort (int *array, int len) {
    for (int i = 0; i < len; i++) {
        for (int j = 0; j < len-i-1; j++){
            if (array[j] > array[j+1]) {
                int temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }
}