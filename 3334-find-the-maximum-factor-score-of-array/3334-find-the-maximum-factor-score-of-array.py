import math
from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0] * nums[0]

        def get_score(arr: List[int]) -> int:
            if not arr:
                return 0
            return math.gcd(*arr) * math.lcm(*arr)

        # Factor score without removing any element
        max_factor_score = get_score(nums)

        # Factor score after removing each element at index i
        for i in range(n):
            sub_arr = nums[:i] + nums[i+1:]
            max_factor_score = max(max_factor_score, get_score(sub_arr))

        return max_factor_score