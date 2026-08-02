class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(land), len(land[0])
        result = []

        for r1 in range(m):
            for c1 in range(n):
                # Check if this cell is farmland AND is the top-left corner of a group
                if land[r1][c1] == 1:
                    is_top_boundary = (r1 == 0 or land[r1 - 1][c1] == 0)
                    is_left_boundary = (c1 == 0 or land[r1][c1 - 1] == 0)

                    if is_top_boundary and is_left_boundary:
                        # Find the bottom boundary (r2)
                        r2 = r1
                        while r2 + 1 < m and land[r2 + 1][c1] == 1:
                            r2 += 1

                        # Find the right boundary (c2)
                        c2 = c1
                        while c2 + 1 < n and land[r1][c2 + 1] == 1:
                            c2 += 1

                        result.append([r1, c1, r2, c2])

        return result