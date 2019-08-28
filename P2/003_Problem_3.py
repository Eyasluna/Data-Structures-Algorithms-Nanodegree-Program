def rearrange_digits(input_list: list, first_layer: bool = False) -> list:
    """
        Rearrange Array Elements so as to form two number such that their sum is maximum.

        Args:
           input_list(list): Input List
           first_layer(bool): placeholder to know if we are in the first layer of the recursion (special case)
        Returns:
           (int),(int): Two maximum sums
        """

    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]

    left = rearrange_digits(left)
    right = rearrange_digits(right)

    return merge(left, right, first_layer)


def merge(left: list, right: list, first_layer: bool = False) -> list:
    outcome = []
    left_int = 0
    right_int = 0

    if first_layer:
        max_left = ''
        max_right = ''
        to_left = True

        while left_int < len(left) and right_int < len(right):
            if left[left_int] > right[right_int]:
                if to_left:
                    max_left = str(right[right_int]) + max_left
                else:
                    max_right = str(right[right_int]) + max_right
                right_int += 1
            else:
                if to_left:
                    max_left = str(left[left_int]) + max_left
                else:
                    max_right = str(left[left_int]) + max_right
                left_int += 1

            to_left = not to_left  # Distribute the numbers on each of the list

        while left_int < len(left):   # left index is not exhausted
            if to_left:
                max_left = str(left[left_int]) + max_left
            else:
                max_right = str(left[left_int]) + max_right

            left_int += 1
            to_left = not to_left

        while right_int < len(right):  # right index is not exhausted
            if to_left:
                max_left = str(right[right_int]) + max_left
            else:
                max_right = str(right[right_int]) + max_right

            right_int += 1
            to_left = not to_left

        return [int(max_left), int(max_right)]

    else:
        while left_int < len(left) and right_int < len(right):
            if left[left_int] > right[right_int]:
                outcome.append(right[right_int])
                right_int += 1
            else:
                outcome.append(left[left_int])
                left_int += 1

        outcome += left[left_int:]
        outcome += right[right_int:]

        return outcome


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")




print('Test 1:')
list_num = [1, 2, 3, 4, 5]
result = rearrange_digits(input_list=list_num, first_layer=True)
if result == [531, 42]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 2:')
list_num = [4, 6, 2, 5, 9, 8]
result = rearrange_digits(input_list=list_num, first_layer=True)
if result == [852, 964]:
    print('Pass \n')
else:
    print("Fail \n")

print('Test 3:')
list_num = [1, 2, 3]
result = rearrange_digits(input_list=list_num, first_layer=True)
if result == [31, 2]:
    print('Pass \n')
else:
    print("Fail \n")


