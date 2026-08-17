class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        if n <= 1:
            return 0

        # Prefix sums for O(1) range sum queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        maxL = [[0] * n for _ in range(n)]
        maxR = [[0] * n for _ in range(n)]

        # Base case for length 1 intervals
        for i in range(n):
            maxL[i][i] = stoneValue[i]
            maxR[i][i] = stoneValue[i]

        # Bottom-up interval DP: length from 2 to n
        for length in range(2, n + 1):
            mid = 0
            for i in range(n - length + 1):
                j = i + length - 1
                if mid < i:
                    mid = i

                # Advance mid while left part sum < right part sum
                total = prefix[j + 1] - prefix[i]
                while mid < j and (prefix[mid + 1] - prefix[i]) * 2 < total:
                    mid += 1

                res = 0
                
                # Case 1: left_sum < right_sum for split points in [i, mid - 1]
                if mid > i:
                    res = max(res, maxL[i][mid - 1])

                # Case 2: left_sum == right_sum at mid
                if (prefix[mid + 1] - prefix[i]) * 2 == total:
                    res = max(res, maxL[i][mid], maxR[mid + 1][j])
                    # Case 3: left_sum > right_sum for split points in [mid + 1, j - 1]
                    if mid + 1 < j:
                        res = max(res, maxR[mid + 2][j])
                else:
                    # Case 3: left_sum > right_sum for split points in [mid, j - 1]
                    if mid < j:
                        res = max(res, maxR[mid + 1][j])

                dp[i][j] = res
                maxL[i][j] = max(maxL[i][j - 1], res + total)
                maxR[i][j] = max(maxR[i + 1][j], res + total)

        return dp[0][n - 1]