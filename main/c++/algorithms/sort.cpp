#include <stdio.h>
#include <string.h>
#include <memory.h>
#include <stdlib.h>

#include "sort.h"

class Sort {

    private:
        int *array;
        int len;

        enum algorithm {
            bubbleSort,
            invalid,
        };

        algorithm hash (char *inString) {
            if (strcmp(inString, "bubble sort") == 0) return bubbleSort;
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
            }
        }

        int *get () {
            return array;
        }
};

int main() {
    int arr[] = {3,1,4,2};
    Sort s(arr);

    s.print();

    s.sort((char *) "bubble sort");

    s.print();

    return 0;
}