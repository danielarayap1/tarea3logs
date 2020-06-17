import math
from random import random

random_list = [int(100 * random()) for i in range(15)]
random_list.sort()


def binary_search(ordered_list, low, hig, target):
    print(f'lista: {ordered_list}')
    print(f'buscando en el tramo {ordered_list[low:hig+1]}')
    i = low
    j = hig - 1
    while i <= j:
        m = math.floor((i+j)/2)
        if ordered_list[m] < target:
            i = m + 1
        elif ordered_list[m] > target:
            j = m - 1
        else:
            return ordered_list[m], ordered_list[m+1]
    print(f'elemento esta entre {ordered_list[j]} y {ordered_list[i]}')
    print(f'entre los indices {j} y {i}')
    return j, i


#print(binary_search(random_list, 5, 15, 56))

"""
function binary_search(A, n, T) is
    L := 0
    R := n − 1
    while L ≤ R do
        m := floor((L + R) / 2)
        if A[m] < T then
            L := m + 1
        else if A[m] > T then
            R := m - 1
        else:
            return m
    return unsuccessful
"""