class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m, n = len(points), len(points[0])
        prev = points[0]

        for r in range(1, m):
            curr = [0] * n
            
            # Pass 1: Left to right (carrying the best previous score decaying by 1 per step)
            left_max = [0] * n
            left_max[0] = prev[0]
            for c in range(1, n):
                left_max[c] = max(left_max[c - 1] - 1, prev[c])

            # Pass 2: Right to left (carrying the best previous score decaying by 1 per step)
            right_max = [0] * n
            right_max[-1] = prev[-1]
            for c in range(n - 2, -1, -1):
                right_max[c] = max(right_max[c + 1] - 1, prev[c])

            # Combine left and right sweeps with current row points
            for c in range(n):
                curr[c] = points[r][c] + max(left_max[c], right_max[c])

            prev = curr

        return max(prev)