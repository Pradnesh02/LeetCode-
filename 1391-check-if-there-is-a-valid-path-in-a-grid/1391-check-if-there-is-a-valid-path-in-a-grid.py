from collections import deque


class Solution:

  def hasValidPath(self, grid: list[list[int]]) -> bool:
    m, n = len(grid), len(grid[0])

    # Direction deltas: (dr, dc)
    # L: (0, -1), R: (0, 1), U: (-1, 0), D: (1, 0)
    # Map each street type to the valid directions it connects to
    pipes = {
        1: [(0, -1), (0, 1)],  # Left, Right
        2: [(-1, 0), (1, 0)],  # Up, Down
        3: [(0, -1), (1, 0)],  # Left, Down
        4: [(0, 1), (1, 0)],  # Right, Down
        5: [(0, -1), (-1, 0)],  # Left, Up
        6: [(0, 1), (-1, 0)],  # Right, Up
    }

    queue = deque([(0, 0)])
    visited = {(0, 0)}

    while queue:
      r, c = queue.popleft()
      if r == m - 1 and c == n - 1:
        return True

      street_type = grid[r][c]
      for dr, dc in pipes[street_type]:
        nr, nc = r + dr, c + dc

        # Check bounds
        if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
          neighbor_type = grid[nr][nc]
          # The neighbor street must have an opening in the opposite direction (-dr, -dc)
          if (-dr, -dc) in pipes[neighbor_type]:
            visited.add((nr, nc))
            queue.append((nr, nc))

    return False