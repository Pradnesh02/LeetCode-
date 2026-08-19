class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        max_score = -1
        best_div = float('inf')
        
        for d in divisors:
            # Count how many elements in nums are divisible by d
            score = sum(1 for x in nums if x % d == 0)
            
            # Update if score is higher, or if tied and the divisor is smaller
            if score > max_score or (score == max_score and d < best_div):
                max_score = score
                best_div = d
                
        return best_div