import sys
from typing import List

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Weight of entering node x
        def get_weight(x: int) -> int:
            return 1 if x % 2 == 1 else 2

        # best[u] will store the top two (distance_down, child_node)
        best = [[(0, -1), (0, -1)] for _ in range(n)]

        # Pass 1: Post-order DFS to compute down distances for all nodes
        def dfs1(u: int, parent: int):
            max1, c1 = 0, -1
            max2, c2 = 0, -1

            for v in adj[u]:
                if v != parent:
                    dfs1(v, u)
                    d = best[v][0][0] + get_weight(v)
                    if d > max1:
                        max2, c2 = max1, c1
                        max1, c1 = d, v
                    elif d > max2:
                        max2, c2 = d, v

            best[u] = [(max1, c1), (max2, c2)]

        dfs1(0, -1)

        ans = [0] * n

        # Pass 2: Pre-order DFS to compute up distances and answer for all roots
        def dfs2(u: int, parent: int, up_dist: int):
            # The answer for node u is the maximum of down distance and up distance
            ans[u] = max(best[u][0][0], up_dist)

            for v in adj[u]:
                if v != parent:
                    # Exclude child v to find the longest branch from u
                    branch_down = best[u][1][0] if best[u][0][1] == v else best[u][0][0]
                    # Moving from child v up to u costs get_weight(u)
                    next_up = max(up_dist, branch_down) + get_weight(u)
                    dfs2(v, u, next_up)

        dfs2(0, -1, 0)
        return ans