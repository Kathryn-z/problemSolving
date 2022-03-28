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
    count = 0
    unique = []

    for i in range(len(nums)):
        if (nums[i] not in unique):
            count+=1
            unique.append(nums[i])
        
    return count


# TODO add your partner's implementation here

def partnerUniqueInts(nums) -> int:
    return -1


# TODO discuss runtime, space usage, and create a solution you are both happy
# with below

def uniqueIntsFinal(nums) -> int:
    return -1
