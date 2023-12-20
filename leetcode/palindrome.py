class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            string = str(x)
            rev_string = string[::-1]
            if rev_string == string:
                return True
            else:
                return False

x = -121
x = 1234321
print(Solution().isPalindrome(x))

def isPalindrome(x: int) -> bool:
    if x < 0 or (x > 0 and x%10 == 0):   # if x is negative, return False. if x is positive and last digit is 0, that also cannot form a palindrome, return False.
        return False

    result = 0
    while x > result:
        result = result * 10 + x % 10
        x = x // 10

    return True if (x == result or x == result // 10) else False

print(isPalindrome(1234321))