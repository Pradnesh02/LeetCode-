class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, val in enumerate(nums):
            digit_sum = sum(int(d) for d in str(val))
            if digit_sum == i:
                return i
        return -1