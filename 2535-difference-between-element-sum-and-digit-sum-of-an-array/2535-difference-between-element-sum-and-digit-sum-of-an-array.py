class Solution(object):
    def differenceOfSum(self, nums):
        element_sum = sum(nums)
        digit_sum = 0
        
        for x in nums:
            while x > 0:
                digit_sum += x % 10
                x //= 10
                
        return abs(element_sum - digit_sum)