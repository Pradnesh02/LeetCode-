from collections import deque

class Solution(object):
    def highestRankedKItems(self, grid, pricing, start, k):
        """
        :type grid: List[List[int]]
        :type pricing: List[int]
        :type start: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(grid), len(grid[0])
        low, high = pricing
        sr, sc = start
        
        visited = set([(sr, sc)])
        queue = deque([(sr, sc, 0)])
        
        candidates = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, dist = queue.popleft()
            price = grid[r][c]
            
            # Check if current cell is an item within the price range
            if price > 1 and low <= price <= high:
                candidates.append((dist, price, r, c))
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check valid adjacent cell (within bounds, not a wall, unvisited)
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
                    
        # Sort by: 1. Distance, 2. Price, 3. Row, 4. Col
        candidates.sort()
        
        return [[r, c] for _, _, r, c in candidates[:k]]