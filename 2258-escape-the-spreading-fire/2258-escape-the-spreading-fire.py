from collections import deque

class Solution(object):
    def maximumMinutes(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        INF = float('inf')

        # 1. Calculate minimum time for fire to reach each cell via Multi-Source BFS
        fire_time = [[INF] * n for _ in range(m)]
        fire_queue = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fire_queue.append((r, c))
                    fire_time[r][c] = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while fire_queue:
            r, c = fire_queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 2:
                    if fire_time[nr][nc] == INF:
                        fire_time[nr][nc] = fire_time[r][c] + 1
                        fire_queue.append((nr, nc))

        # Helper function to test if we can reach (m-1, n-1) after waiting 'wait_time' minutes
        def can_escape(wait_time):
            # If fire reaches (0, 0) before or at wait_time, we can't even start
            if fire_time[0][0] <= wait_time:
                return False

            queue = deque([(0, 0, wait_time)])
            visited = set([(0, 0)])

            while queue:
                r, c, time = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 2:
                        if (nr, nc) not in visited:
                            next_time = time + 1

                            # Safehouse rule: player can reach safehouse at the exact same time as fire
                            if nr == m - 1 and nc == n - 1:
                                if next_time <= fire_time[nr][nc]:
                                    return True
                            else:
                                # For normal cells, player must arrive strictly before fire
                                if next_time < fire_time[nr][nc]:
                                    visited.add((nr, nc))
                                    queue.append((nr, nc, next_time))

            return False

        # 2. Binary search for the maximum wait time in range [0, m * n]
        low, high = 0, m * n
        best = -1

        while low <= high:
            mid = (low + high) // 2
            if can_escape(mid):
                best = mid
                low = mid + 1
            else:
                high = mid - 1

        # If we can wait up to m*n minutes, we can wait indefinitely (10^9)
        return 10**9 if best == m * n else best