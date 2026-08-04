class Solution(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # Pair each element with its cost and sort by value
        pairs = sorted(zip(nums, cost))
        
        # Calculate the total weight sum
        total_weight = sum(cost)
        half_weight = (total_weight + 1) // 2
        
        # Find the weighted median
        accumulated_weight = 0
        target = pairs[0][0]
        
        for num, c in pairs:
            accumulated_weight += c
            if accumulated_weight >= half_weight:
                target = num
                break
                
        # Calculate the minimum total cost using the weighted median
        return sum(abs(num - target) * c for num, c in zip(nums, cost))