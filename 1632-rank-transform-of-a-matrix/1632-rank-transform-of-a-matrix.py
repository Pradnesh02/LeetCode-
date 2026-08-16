from collections import defaultdict

class Solution(object):
    def matrixRankTransform(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        
        # Group coordinates by their value
        val_to_cells = defaultdict(list)
        for r in range(m):
            for c in range(n):
                val_to_cells[matrix[r][c]].append((r, c))
                
        rank = [0] * (m + n)
        ans = [[0] * n for _ in range(m)]
        
        # Process unique values in ascending order
        for val in sorted(val_to_cells.keys()):
            parent = {}
            
            def find(i):
                if parent[i] != i:
                    parent[i] = find(parent[i])
                return parent[i]
            
            def union(i, j):
                parent.setdefault(i, i)
                parent.setdefault(j, j)
                pi, pj = find(i), find(j)
                if pi != pj:
                    parent[pi] = pj
            
            # Union row index r and column index (c + m) for cells with the same value
            for r, c in val_to_cells[val]:
                union(r, c + m)
                
            # Find the max rank required across connected components
            max_rank = defaultdict(int)
            for r, c in val_to_cells[val]:
                root = find(r)
                max_rank[root] = max(max_rank[root], rank[r], rank[c + m])
                
            # Assign (max_rank + 1) to cells and update the row/column ranks
            for r, c in val_to_cells[val]:
                res = max_rank[find(r)] + 1
                ans[r][c] = res
                rank[r] = res
                rank[c + m] = res
                
        return ans