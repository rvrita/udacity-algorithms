def rotated_array_search(input_list, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1

    idx_L = 0
    idx_R = idx_M = len(input_list) - 1

    while True:
        L = input_list[idx_L]
        R = input_list[idx_R]
        idx_M = (idx_L + idx_R) // 2
        # print(input_list[idx_L:idx_R+1], idx_L, idx_M, idx_R)
        M = input_list[idx_M]

        if target == M:
            return idx_M
        elif target == R:
            return idx_R
        elif idx_L == idx_M:
            return -1
        elif L < M: # left half continuous
            if target >= L and target <= M:
                idx_R = idx_M
            else:
                idx_L = idx_M + 1
        elif M < R: # right half continuous
            if target >= M and target <= R:
                idx_L = idx_M + 1
            else:
                idx_R = idx_M


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[], 10])
test_function([[1, 2], 1])
test_function([[2, 1], 1])
test_function([[1, 2], 2])
test_function([[2, 1], 2])
test_function([[2, 3, 4, 1], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 4])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[7, 8, 9, 10, 1, 2, 3, 4, 5, 6], 2])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4, 5], 6])
