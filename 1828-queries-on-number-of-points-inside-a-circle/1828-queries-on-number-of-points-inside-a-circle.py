class Solution(object):
    def countPoints(self, points, queries):
        res = []
        
        for xc, yc, r in queries:
            r_sq = r * r
            count = 0
            for x, y in points:
                if (x - xc) ** 2 + (y - yc) ** 2 <= r_sq:
                    count += 1
            res.append(count)
            
        return res