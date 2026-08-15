class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        path = []
        
        def backtrack(start, remain):
            if len(path) == k:
                if remain == 0:
                    result.append(list(path))
                return
            
            # Prune: upper bound ensures enough remaining digits are available
            upper_bound = 9 - (k - len(path)) + 1
            for num in range(start, upper_bound + 1):
                if num > remain:
                    break  # Further numbers will only be larger
                
                path.append(num)
                backtrack(num + 1, remain - num)
                path.pop()
                
        backtrack(1, n)
        return result