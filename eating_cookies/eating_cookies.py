'''
Input: an integer
Returns: an integer
'''


def eating_cookies(cookies):
    print(cookies)
    if cookies == 0:
        return 1
    if cookies < 0:
        return 0
    return eating_cookies(cookies-1) + eating_cookies(cookies-2) + eating_cookies(cookies-3)
    # ITERATIVE WORKING WITH BIG NUMBERS


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

# 3
# 1
# 2 1
# 1
# 1 1
# 2
# 1 1

# 3 1
