from collections import deque


class Solution:

    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        found = False

        # Step 1: DFS to find and mark the first island, adding its cells to the BFS queue
        def dfs(r: int, c: int):
            grid[r][c] = 2
            queue.append((r, c, 0))
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    dfs(nr, nc)

        for r in range(n):
            if found:
                break
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c)
                    found = True
                    break

        # Step 2: Multi-source BFS to expand from the first island until reaching the second
        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if grid[nr][nc] == 1:
                        return dist
                    elif grid[nr][nc] == 0:
                        grid[nr][nc] = 2  # Mark as visited
                        queue.append((nr, nc, dist + 1))

        return 0