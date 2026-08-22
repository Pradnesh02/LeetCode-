class Solution(object):
    def imageSmoother(self, img):
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                total_sum = 0
                count = 0
                
                # Check the 3x3 surrounding neighborhood
                for dr in (-1, 0, 1):
                    for dc in (-1, 0, 1):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < m and 0 <= nc < n:
                            total_sum += img[nr][nc]
                            count += 1
                            
                result[r][c] = total_sum // count
                
        return result