class Solution(object):
    def countLatticePoints(self, circles):
        points = set()
        
        for xc, yc, r in circles:
            r_sq = r * r
            for x in range(xc - r, xc + r + 1):
                for y in range(yc - r, yc + r + 1):
                    if (x - xc) ** 2 + (y - yc) ** 2 <= r_sq:
                        points.add((x, y))
                        
        return len(points)