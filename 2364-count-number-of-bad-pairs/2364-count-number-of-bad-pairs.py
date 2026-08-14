from collections import defaultdict

class Solution(object):
    def countBadPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total_pairs = n * (n - 1) // 2
        good_pairs = 0
        diff_count = defaultdict(int)

        for i, num in enumerate(nums):
            diff = num - i
            # If we've seen this diff before, each occurrence forms a good pair with the current element
            good_pairs += diff_count[diff]
            diff_count[diff] += 1

        return total_pairs - good_pairs