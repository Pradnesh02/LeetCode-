from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # If the number of unique elements is less than total elements, a duplicate exists
        return len(set(nums)) < len(nums)