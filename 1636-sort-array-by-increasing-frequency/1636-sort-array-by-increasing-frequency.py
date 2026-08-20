from collections import Counter

class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = Counter(nums)
        # Sort by frequency ascending, then by value descending
        return sorted(nums, key=lambda x: (freq[x], -x))