from collections import Counter

class Solution(object):
    def getLargestOutlier(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        counts = Counter(nums)
        max_outlier = float('-inf')

        # Try assuming each number x in nums is the outlier
        for x in nums:
            # Remainder after removing the candidate outlier x
            rem = total_sum - x
            
            # The sum element must be equal to rem / 2
            if rem % 2 == 0:
                s = rem // 2
                
                # Check if the sum element `s` exists in nums
                # If s == x, we need at least 2 occurrences of x in nums
                if (s != x and counts[s] > 0) or (s == x and counts[x] > 1):
                    max_outlier = max(max_outlier, x)

        return max_outlier