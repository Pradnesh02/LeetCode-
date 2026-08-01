class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        # memoization table for subproblems (i, j)
        memo = {}

        def maxDiff(i, j):
            if i == j:
                return nums[i]
            
            if (i, j) in memo:
                return memo[(i, j)]

            # Option 1: Pick nums[i] from the start
            pick_left = nums[i] - maxDiff(i + 1, j)
            # Option 2: Pick nums[j] from the end
            pick_right = nums[j] - maxDiff(i, j - 1)

            memo[(i, j)] = max(pick_left, pick_right)
            return memo[(i, j)]

        # Player 1 wins if the relative score difference is >= 0
        return maxDiff(0, n - 1) >= 0