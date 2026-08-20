from collections import Counter

class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts = Counter(nums)
        return all(count % 2 == 0 for count in counts.values())