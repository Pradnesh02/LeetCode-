from collections import deque

class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        # Build adjacency list for directed graph: u -> v
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
            
        # Phase 1: BFS from k to find all suspicious methods
        suspicious = set([k])
        queue = deque([k])
        
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        # Phase 2: Check if any non-suspicious node invokes a suspicious node
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                # Cannot remove suspicious methods; return all methods
                return list(range(n))
                
        # Return only the non-suspicious methods
        return [i for i in range(n) if i not in suspicious]