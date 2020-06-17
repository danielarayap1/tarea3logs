import math

from binary_search import binary_search
from random import random

random_list = [int(100 * random()) for i in range(40)]
random_list.sort()


def doubling_search(ordered_list, size, target):
    print(ordered_list)
    if size == 0:
        return
    bound = 1
    while bound < size and ordered_list[bound] < target:
        print(f'bound: {bound}')
        print(f'{target} es mayor que {ordered_list[bound]}')
        bound *= 2
    print(f'{target} es menor que {ordered_list[bound]}! ')
    print(f'running binary search entre {ordered_list[int(bound/2)]} y {ordered_list[bound]}')
    return binary_search(ordered_list, int(bound/2), min(bound + 1, size), target)


doubling_search(random_list, 15, 56)

"""
template <typename T>
int exponential_search(T arr[], int size, T key){
    if (size == 0)
        return NOT_FOUND;
    int bound = 1;
    while (bound < size && arr[bound] < key) {
        bound *= 2;
    }
    return binary_search(arr, key, bound/2, min(bound + 1, size));
}
"""
