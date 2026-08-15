class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        path = []
        
        def backtrack(start, remain):
            if remain == 0:
                result.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break  # Prune search space
                
                path.append(candidates[i])
                # Stay at index i to allow reusing the same candidate
                backtrack(i, remain - candidates[i])
                path.pop()
                
        backtrack(0, target)
        return result