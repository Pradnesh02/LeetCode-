import sys
from typing import List

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        ans = [0] * n
        count = [1] * n  # count[i] stores the size of the subtree rooted at i

        # Pass 1: Post-order traversal to compute subtree sizes and ans[0]
        def dfs1(u: int, parent: int):
            for v in adj[u]:
                if v != parent:
                    dfs1(v, u)
                    count[u] += count[v]
                    ans[u] += ans[v] + count[v]

        dfs1(0, -1)

        # Pass 2: Pre-order traversal to compute the answer for all other nodes
        def dfs2(u: int, parent: int):
            for v in adj[u]:
                if v != parent:
                    # Rerooting formula
                    ans[v] = ans[u] - count[v] + (n - count[v])
                    dfs2(v, u)

        dfs2(0, -1)
        return ans