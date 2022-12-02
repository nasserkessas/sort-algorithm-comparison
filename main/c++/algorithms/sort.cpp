#include <stdio.h>
#include <string.h>
#include <memory.h>
#include <stdlib.h>

#include "sort.h"

#define ARRAY_LENGTH 100

class Sort {

    private:
        int *array;
        int len;

        enum algorithm {
            bubbleSort,
            combSort,
            invalid,
        };

        algorithm hash (char *inString) {
            if (strcmp(inString, "bubble sort") == 0) return bubbleSort;
            if (strcmp(inString, "comb sort") == 0) return combSort;
            return invalid;
        }

    public:
        template<std::size_t arr_len>
        Sort (int (&arr)[arr_len]) {
            len = arr_len;
            array = (int *) malloc(len * sizeof(int));
            memcpy(array, arr, len * sizeof(int));
        };

        void print () {
            for (int i = 0; i < len; i++) {
                printf("%d ", array[i]);
            }
            printf("\n");
        }

        void sort (char *algorithm) {
            switch (hash(algorithm)) {
            case bubbleSort:
                array = bubble_sort(array, len);
                break;

            case combSort:
                array = comb_sort(array, len);
                break;

            case invalid:
                exit(1);
            }
        }

        int *get () {
            return array;
        }
};

int main() {
    int arr[ARRAY_LENGTH];

    for (int i = 0; i < ARRAY_LENGTH; i++) {
        arr[i] = i+1;
    }

    shuffle(arr, (size_t) ARRAY_LENGTH);

    Sort s(arr);

    s.print();

    s.sort((char *) "comb sort");

    s.print();

    return 0;
}