class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        path = []
        
        def backtrack(start):
            if len(path) == k:
                result.append(list(path))
                return
            
            # Prune search space: ensure enough numbers remain to complete the combination
            upper_bound = n - (k - len(path)) + 1
            for num in range(start, upper_bound + 1):
                path.append(num)
                backtrack(num + 1)
                path.pop()
                
        backtrack(1)
        return result