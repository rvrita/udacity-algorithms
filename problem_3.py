def mergesort(items):

    if len(items) <= 1:
        return items

    idx_M = len(items) // 2
    left = items[:idx_M]
    right = items[idx_M:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)

def merge(left, right):

    merged = []
    idx_L = 0
    idx_R = 0

    while idx_L < len(left) and idx_R < len(right):
        if left[idx_L] < right[idx_R]:
            merged.append(right[idx_R])
            idx_R += 1
        else:
            merged.append(left[idx_L])
            idx_L += 1

    merged += left[idx_L:]
    merged += right[idx_R:]

    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list is None or len(input_list) < 2:
        return [-1]

    sorted_list = mergesort(input_list)
    num1 = ''
    num2 = ''

    for i in range(len(sorted_list)):
        if i % 2 == 0:
            num1 += str(sorted_list[i])
        else:
            num2 += str(sorted_list[i])

    return [int(num1), int(num2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([None, [-1]])
test_function([[], [-1]])
test_function([[0], [-1]])
test_function([[0, 0], [0, 0]])
test_function([[9, 8], [9, 8]])
test_function([[9, 7, 8], [98, 7]])
test_function([[6, 7, 8], [87, 6]])
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
