from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0

        # Step 1: Initialize the queue with all initial rotten oranges (2)
        # and count the total number of fresh oranges (1)
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # If there are no fresh oranges to rot, return 0 immediately
        if fresh_count == 0:
            return 0

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Step 2: Multi-Source Breadth-First Search (BFS)
        while queue and fresh_count > 0:
            minutes += 1
            # Process all rotten oranges at the current minute level
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # If adjacent cell is within bounds and contains a fresh orange
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Turn it rotten
                        fresh_count -= 1   # Decrement fresh orange count
                        queue.append((nr, nc))

        # Step 3: If fresh oranges remain unreachable, return -1; otherwise return minutes
        return minutes if fresh_count == 0 else -1