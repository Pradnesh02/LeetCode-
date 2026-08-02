class Solution(object):
    def stoneGame(self, piles):
        n = len(piles)
        memo = {}

        def maxDiff(i, j):
            if i == j:
                return piles[i]
            if (i, j) in memo:
                return memo[(i, j)]

            pick_left = piles[i] - maxDiff(i + 1, j)
            pick_right = piles[j] - maxDiff(i, j - 1)

            memo[(i, j)] = max(pick_left, pick_right)
            return memo[(i, j)]

        return maxDiff(0, n - 1) > 0