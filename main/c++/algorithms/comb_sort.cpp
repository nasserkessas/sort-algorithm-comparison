#include <cmath>

#include "sort.h"

int *comb_sort (int *array, int len) {
    int gap = len;
    bool swapped = true;
    while (gap !=1 || swapped == false) {
        gap = floor((gap * 10)/13);
        if (gap < 1) {
            gap = 1;
        }

        swapped = false;
        for (int i = 0; i < len-gap; i++) {
            if (array[i] > array[i + gap]) {
                int temp = array[i];
                array[i] = array[i + gap];
                array[i + gap] = temp;
                swapped = true;
            }
        }
    }
    return array;
}