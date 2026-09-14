class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Sort primarily by x ascending, secondarily by y descending
        points.sort(key=lambda p: (p[0], -p[1]))
        
        n = len(points)
        count = 0
        
        for i in range(n):
            y_A = points[i][1]
            max_y = float('-inf')
            
            for j in range(i + 1, n):
                y_B = points[j][1]
                
                # B must be below or level with A
                if y_B <= y_A:
                    if y_B > max_y:
                        count += 1
                        max_y = y_B
                        
        return count