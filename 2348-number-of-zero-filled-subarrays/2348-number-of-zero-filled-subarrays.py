class Solution(object):
    def zeroFilledSubarray(self, nums):
        total = 0
        consecutive_zeros = 0

        for x in nums:
            if x == 0:
                consecutive_zeros += 1
                total += consecutive_zeros
            else:
                consecutive_zeros = 0

        return total