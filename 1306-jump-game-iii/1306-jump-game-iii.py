from collections import deque


class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        queue = deque([start])
        visited = set([start])

        while queue:
            curr = queue.popleft()

            # Target reached
            if arr[curr] == 0:
                return True

            # Explore forward and backward jumps
            for next_idx in (curr + arr[curr], curr - arr[curr]):
                if 0 <= next_idx < n and next_idx not in visited:
                    visited.add(next_idx)
                    queue.append(next_idx)

        return False