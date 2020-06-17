import math
from random import random

random_list = [int(100 * random()) for i in range(15)]
random_list.sort()


def sequential_search(ordered_list, target):
    print(ordered_list)
    i = 0
    while i < len(ordered_list):
        if target > ordered_list[i]:
            print(f'{target} mayor que {ordered_list[i]}, sigue')
        elif target <= ordered_list[i]:
            print(f'elemento esta entre {ordered_list[i]} y {ordered_list[i+1]}')
            return i, i+1
        i += 1
    return i, i+1
    
    
print(sequential_search(random_list, 56))


"""
Given a list L of n elements with values or records L0 .... Ln−1, and target value T, the following subroutine uses linear search to find the index of the target T in L.[3]

    Set i to 0.
    If Li = T, the search terminates successfully; return i.
    Increase i by 1.
    If i < n, go to step 2. Otherwise, the search terminates unsuccessfully.
"""