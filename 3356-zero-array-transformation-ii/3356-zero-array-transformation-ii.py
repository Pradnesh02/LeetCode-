class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        n = len(nums)
        m = len(queries)
        
        # Helper function to check if the first k queries can reduce nums to 0
        def can_make_zero(k):
            diff = [0] * (n + 1)
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                diff[r + 1] -= val
            
            curr_capacity = 0
            for i in range(n):
                curr_capacity += diff[i]
                if curr_capacity < nums[i]:
                    return False
            return True

        # Binary search for the minimum k in range [0, m]
        low, high = 0, m
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if can_make_zero(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans