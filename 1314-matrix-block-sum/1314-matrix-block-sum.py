from typing import List

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        # Build (m + 1) x (n + 1) prefix sum matrix
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            for c in range(n):
                P[r + 1][c + 1] = mat[r][c] + P[r][c + 1] + P[r + 1][c] - P[r][c]
                
        answer = [[0] * n for _ in range(m)]
        
        # Calculate sum for each block in O(1)
        for i in range(m):
            for j in range(n):
                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(m - 1, i + k)
                c2 = min(n - 1, j + k)
                
                answer[i][j] = (
                    P[r2 + 1][c2 + 1]
                    - P[r1][c2 + 1]
                    - P[r2 + 1][c1]
                    + P[r1][c1]
                )
                
        return answer