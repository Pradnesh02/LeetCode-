from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        
        # Build the graph
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val
            
        def bfs(start: str, end: str) -> float:
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
                
            queue = deque([(start, 1.0)])
            visited = {start}
            
            while queue:
                curr, product = queue.popleft()
                if curr == end:
                    return product
                
                for neighbor, weight in graph[curr].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, product * weight))
                        
            return -1.0
        
        return [bfs(src, dst) for src, dst in queries]