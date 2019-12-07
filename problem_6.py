def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_el = ints[0]
    max_el = ints[0]

    for i in range(len(ints)):
        if min_el > ints[i]:
            min_el = ints[i]
        elif max_el < ints[i]:
            max_el = ints[i]
    return (min_el,max_el)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((5, 5) == get_min_max([5])) else "Fail")
print ("Pass" if ((-1, 1) == get_min_max([1, -1])) else "Fail")
