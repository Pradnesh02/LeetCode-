class Solution(object):
    def specialPerm(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(nums)
        memo = {}

        def dp(mask, prev):
            # Base Case: all numbers placed
            if mask == (1 << n) - 1:
                return 1
            
            state = (mask, prev)
            if state in memo:
                return memo[state]

            total = 0
            for i in range(n):
                # Check if nums[i] is not yet used
                if not (mask & (1 << i)):
                    # Check divisibility condition
                    if prev == -1 or nums[prev] % nums[i] == 0 or nums[i] % nums[prev] == 0:
                        total = (total + dp(mask | (1 << i), i)) % MOD

            memo[state] = total
            return total

        return dp(0, -1)