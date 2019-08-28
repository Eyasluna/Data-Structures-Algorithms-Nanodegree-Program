def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    j = 0
    null = 0
    k = len(input_list) - 1

    while j <= k:
        if input_list[j] == 0:
            input_list[j] = input_list[null]
            input_list[null] = 0
            null += 1
            j += 1

        elif input_list[j] == 2:
            temp_val = input_list[k]
            input_list[k] = 2
            input_list[j] = temp_val
            k -= 1

        else:
            j += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
print('\n')


test_function([0, 1, 1, 0, 1])
test_function([0, 0, 0])
test_function([])
