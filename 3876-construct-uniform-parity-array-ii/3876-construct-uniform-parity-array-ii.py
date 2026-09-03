class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # If all numbers are even, or the global minimum is odd
        min_val = min(nums1)
        return min_val % 2 == 1 or all(x % 2 == 0 for x in nums1)