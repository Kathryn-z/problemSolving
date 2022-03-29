'''
    Given a string s, determine if it is a valid palindrome or not

    Example
    s = 'racecar'

    if we flip racecar, we get racecar, which is the same as our input
    this makes it a palindrome

    Example2
    s = 'abc'
    
    the flip of 'abc' is 'cba', which is not the same as the input
    this is NOT a palindrome

    Constraints (ok this doesn't matter)
    len(s) < 100,000

    Problem Link
    https://binarysearch.com/problems/Check-Palindrome
'''

# TODO fill in the following with your own implementation

def checkPalindrome(s) -> bool:
    n = len(s)
    for i in range(n):
        if (s[i] != s[n-1-i]):
            return False
    return True

# O(n)

# TODO fill in the following with your partner's implementation

def partnerCheckPalindrome(s) -> bool:
    return s == s[::-1]
# O(n)

# TODO discuss the runtime, space usage, and possible improvements to the
# solutions you came up with

def checkPalindromeFinal(s) -> bool:
    return False
