'''
    Given a list of sorted integers nums, return the number of unique integers
    in the list

    Example
    nums = [2, 2, 2, 3, 4, 6, 6]

    the unique numbers are [2, 3, 4, 6]
    there are 4 unique numbers
    Output > 4

    Constraints
    n <= 10**6 where n is the length of nums

    Problem Link
    https://binarysearch.com/problems/Unique-Integers-in-Sorted-List
    
'''

# TODO add your own implementation below

def uniqueInts(nums) -> int:
    low = 0
    high = 0

    while (high < len(nums)):
        nums[low] = nums[high]
        if (low > 0 and nums[low] == nums[low-1]):
            low-=1
        low+=1
        high+=1

    return low

# TODO my second implementation below

def uniqueInts(nums) -> int:
    return len(set(nums))

# TODO add your partner's implementation here

def partnerUniqueInts(nums) -> int:
    return len(set(nums))


# TODO discuss runtime, space usage, and create a solution you are both happy
# with below

def uniqueIntsFinal(nums) -> int:
    return -1
