from collections import deque

class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        queue = deque()
        
        # Add all land cells (1s) to the multi-source BFS queue
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    
        # If the grid contains only water or only land, return -1
        if len(queue) == 0 or len(queue) == n * n:
            return -1
            
        distance = -1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Multi-source Breadth-First Search (BFS)
        while queue:
            distance += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # If neighbor is within bounds and is an unvisited water cell (0)
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1  # Mark as visited
                        queue.append((nr, nc))
                        
        return distance