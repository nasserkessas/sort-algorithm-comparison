#include <stdlib.h>
#include <time.h>

#include "sort.h"

void shuffle(int *array, int len) {
    srand(time(NULL));
    if (len > 1) {
        for (int i = 0; i < len - 1; i++) {
          int j = i + rand() / (RAND_MAX / (len - i) + 1);
          int temp = array[j];
          array[j] = array[i];
          array[i] = temp;
        }
    }
}