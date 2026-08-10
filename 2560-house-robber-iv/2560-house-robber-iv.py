class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def can_rob(capability):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= capability:
                    count += 1
                    i += 2  # Skip adjacent house
                else:
                    i += 1
            return count >= k

        low, high = min(nums), max(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if can_rob(mid):
                ans = mid
                high = mid - 1  # Try to find a smaller capability
            else:
                low = mid + 1   # Increase capability

        return ans