class Solution:

    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # dp[i] stores the maximum jumps to reach index i from index 0
        dp = [-1] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                # Only consider previous indices that are reachable
                if dp[j] != -1 and -target <= nums[i] - nums[j] <= target:
                    dp[i] = max(dp[i], dp[j] + 1)

        return dp[-1]