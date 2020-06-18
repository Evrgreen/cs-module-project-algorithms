'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    length = len(arr)
    count = 0 
    for number in range(length):
        if arr[number] != 0:
            arr[count] = arr[number]
            count += 1
    while count < length:
        arr[count] = 0
        count += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    print(moving_zeroes([0, 0, 0, 0, 3, 2, 1]))



#TakeAway:
#Original idea was to have arrays popping and appending to each other, not only is that not very time effiecient it also created several issues with mutation that were complicating the solve
#went with 2 loops as a simple save 