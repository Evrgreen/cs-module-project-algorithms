'''
Input: a List of integers
Returns: a List of integers
'''


def product_of_all_other_numbers(arr):
    # Your code here
    # initialize an answer array with 0's equal to array length
    results = [0] * len(arr)
    # initalize the running product total, set to 1 to make multiplication easier
    total = 1
    # running through each element and adding the current value of total* the element to total
    for i in range(len(arr)):
        total = total * arr[i]
    # dividing product by each item and assigning it to the results array
    for item in range(len(arr)):
        results[item] = int(total/arr[item])

    return results


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
