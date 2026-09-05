from collections import defaultdict
from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Step 1: Find the unique path from Bob to node 0 using DFS
        bob_time = {}

        def find_bob_path(u: int, parent: int, time: int) -> bool:
            if u == 0:
                bob_time[u] = time
                return True
            for v in adj[u]:
                if v != parent:
                    if find_bob_path(v, u, time + 1):
                        bob_time[u] = time
                        return True
            return False

        find_bob_path(bob, -1, 0)

        # Step 2: DFS for Alice to find the maximum net income reaching any leaf
        max_income = float('-inf')

        def dfs_alice(u: int, parent: int, time: int, current_income: int):
            nonlocal max_income

            # Calculate income gained/lost at node u
            if u not in bob_time or time < bob_time[u]:
                current_income += amount[u]
            elif time == bob_time[u]:
                current_income += amount[u] // 2
            # If time > bob_time[u], income added is 0

            # Check if current node is a leaf (other than node 0)
            is_leaf = True
            for v in adj[u]:
                if v != parent:
                    is_leaf = False
                    dfs_alice(v, u, time + 1, current_income)

            if is_leaf:
                max_income = max(max_income, current_income)

        dfs_alice(0, -1, 0, 0)
        return max_income