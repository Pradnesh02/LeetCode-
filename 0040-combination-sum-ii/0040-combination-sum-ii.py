class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        results = []

        def backtrack(start, remaining, current_combination):
            if remaining == 0:
                results.append(list(current_combination))
                return

            for i in range(start, len(candidates)):
                # If the candidate exceeds the remaining sum, stop the loop (pruning)
                if candidates[i] > remaining:
                    break
                
                # Skip duplicate elements at the same recursion depth
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current_combination.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], current_combination)
                current_combination.pop()

        backtrack(0, target, [])
        return results