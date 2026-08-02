from collections import defaultdict, deque

class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        n = len(bombs)
        adj = defaultdict(list)

        # Step 1: Build a directed adjacency list
        # Bomb i can detonate Bomb j if distance(i, j)^2 <= radius_i^2
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                
                # Check Euclidean distance squared to avoid floating point imprecision
                dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if dist_sq <= r1 ** 2:
                    adj[i].append(j)

        # Step 2: BFS helper function to count detonated bombs starting from a given bomb
        def get_detonated_count(start_node):
            queue = deque([start_node])
            visited = {start_node}

            while queue:
                curr = queue.popleft()
                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            return len(visited)

        # Step 3: Try starting the chain reaction from every bomb
        max_bombs = 0
        for i in range(n):
            max_bombs = max(max_bombs, get_detonated_count(i))

        return max_bombs