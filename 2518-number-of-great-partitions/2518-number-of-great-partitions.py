class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7

        # If the total sum cannot even support two groups of size at least k
        if sum(nums) < 2 * k:
            return 0

        # dp[s] stores the number of subsets with sum equal to s
        dp = [0] * k
        dp[0] = 1

        for x in nums:
            for s in range(k - 1, x - 1, -1):
                dp[s] = (dp[s] + dp[s - x]) % MOD

        # Total number of partitions into two groups is 2^n
        total_subsets = pow(2, len(nums), MOD)

        # Invalid partitions where the first group has sum < k
        invalid_first_group = sum(dp) % MOD

        # By symmetry, the number of partitions where the second group has sum < k
        # is also invalid_first_group. Since total_sum >= 2*k, both groups cannot
        # simultaneously have sum < k, so there is no overlap to add back.
        ans = (total_subsets - 2 * invalid_first_group) % MOD

        return ans