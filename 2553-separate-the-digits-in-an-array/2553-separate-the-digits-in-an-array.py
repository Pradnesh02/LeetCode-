class Solution(object):
    def separateDigits(self, nums):
        ans = []
        for x in nums:
            digits = []
            while x > 0:
                digits.append(x % 10)
                x //= 10
            ans.extend(reversed(digits))
        return ans