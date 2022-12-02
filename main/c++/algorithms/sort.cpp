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
            selectionSort,
            insertionSort,
            heapSort,
            invalid,
        };

        algorithm hash (char *inString) {
            if (strcmp(inString, "bubble sort") == 0) return bubbleSort;
            if (strcmp(inString, "comb sort") == 0) return combSort;
            if (strcmp(inString, "selection sort") == 0) return selectionSort;
            if (strcmp(inString, "insertion sort") == 0) return insertionSort;
            if (strcmp(inString, "heap sort") == 0) return heapSort;
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
                bubble_sort(array, len);
                break;

            case combSort:
                comb_sort(array, len);
                break;
            
            case selectionSort:
                selection_sort(array, len);
                break;

            case insertionSort:
                insertion_sort(array, len);
                break;

            case heapSort:
                heap_sort(array, len);
                break;

            case invalid:
                printf("Unknown sorting algorithm: \"%s\"", algorithm);
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

    s.sort((char *) "heap sort");

    s.print();

    return 0;
}