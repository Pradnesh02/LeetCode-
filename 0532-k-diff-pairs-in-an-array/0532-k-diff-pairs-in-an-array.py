from collections import Counter

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counts = Counter(nums)
        ans = 0

        if k == 0:
            for val in counts:
                if counts[val] >= 2:
                    ans += 1
        else:
            for val in counts:
                if (val + k) in counts:
                    ans += 1

        return ans