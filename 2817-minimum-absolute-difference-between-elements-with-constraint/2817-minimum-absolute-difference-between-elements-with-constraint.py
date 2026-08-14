from sortedcontainers import SortedList

class Solution(object):
    def minAbsoluteDifference(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        sl = SortedList()
        min_diff = float('inf')

        for i in range(x, len(nums)):
            # Add the element that is now at least x indices away
            sl.add(nums[i - x])
            
            val = nums[i]
            # Find the position of the closest element >= val
            idx = sl.bisect_left(val)

            # Check the element >= val
            if idx < len(sl):
                min_diff = min(min_diff, sl[idx] - val)

            # Check the element < val
            if idx > 0:
                min_diff = min(min_diff, val - sl[idx - 1])

            # Early exit if 0 is found (minimum possible difference)
            if min_diff == 0:
                return 0

        return min_diff