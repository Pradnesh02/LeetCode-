class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
            
        start = 0
        max_len = 0
        
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Length of valid palindrome found is (right - 1) - (left + 1) + 1 = right - left - 1
            return left + 1, right - left - 1

        for i in range(len(s)):
            # Odd length palindromes
            l1, len1 = expand_around_center(i, i)
            if len1 > max_len:
                start = l1
                max_len = len1
                
            # Even length palindromes
            l2, len2 = expand_around_center(i, i + 1)
            if len2 > max_len:
                start = l2
                max_len = len2
                
        return s[start:start + max_len]