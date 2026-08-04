import bisect

class Solution(object):
    def minOperations(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        n = len(nums)
        
        # Build prefix sum array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            
        ans = []
        for q in queries:
            # Find insertion point for q in sorted nums
            i = bisect.bisect_left(nums, q)
            
            # Operations for elements smaller than q
            left_ops = i * q - prefix[i]
            
            # Operations for elements greater than or equal to q
            right_ops = (prefix[n] - prefix[i]) - (n - i) * q
            
            ans.append(left_ops + right_ops)
            
        return ans