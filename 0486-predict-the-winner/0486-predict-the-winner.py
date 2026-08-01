class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        memo = {}

        def maxDiff(i, j):
            # Base case: only one element left
            if i == j:
                return nums[i]
            
            if (i, j) in memo:
                return memo[(i, j)]

            # Option 1: Pick the element at the start (i)
            pick_left = nums[i] - maxDiff(i + 1, j)
            
            # Option 2: Pick the element at the end (j)
            pick_right = nums[j] - maxDiff(i, j - 1)

            # Store and return the maximum relative score possible
            memo[(i, j)] = max(pick_left, pick_right)
            return memo[(i, j)]

        # Player 1 wins if relative score difference is >= 0
        return maxDiff(0, n - 1) >= 0