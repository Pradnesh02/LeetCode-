class Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        """
        :type startPos: List[int]
        :type homePos: List[int]
        :type rowCosts: List[int]
        :type colCosts: List[int]
        :rtype: int
        """
        r0, c0 = startPos
        r1, c1 = homePos

        total_cost = 0

        # Row movement cost
        step_r = 1 if r1 >= r0 else -1
        for r in range(r0 + step_r, r1 + step_r, step_r):
            total_cost += rowCosts[r]

        # Column movement cost
        step_c = 1 if c1 >= c0 else -1
        for c in range(c0 + step_c, c1 + step_c, step_c):
            total_cost += colCosts[c]

        return total_cost