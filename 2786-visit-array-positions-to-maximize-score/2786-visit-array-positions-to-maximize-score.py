class Solution:

    def maxScore(self, nums: List[int], x: int) -> int:
        # dp[0] tracks maximum score ending at an even number
        # dp[1] tracks maximum score ending at an odd number
        dp = [-float("inf"), -float("inf")]

        # Base case: we must start at index 0
        dp[nums[0] % 2] = nums[0]

        for num in nums[1:]:
            parity = num % 2
            # Transition: take num either coming from the same parity or different parity (costs x)
            dp[parity] = max(
                dp[parity] + num,
                dp[1 - parity] + num - x,
            )

        return max(dp[0], dp[1])