class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes (e.g., -121 reads as 121-)
        # Numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even length numbers: x == reversed_half
        # For odd length numbers: x == reversed_half // 10 (middle digit doesn't matter)
        return x == reversed_half or x == reversed_half // 10