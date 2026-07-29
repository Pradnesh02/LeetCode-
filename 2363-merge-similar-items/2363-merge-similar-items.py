from collections import defaultdict

class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        weights = defaultdict(int)
        
        # Aggregate weights for items1
        for val, weight in items1:
            weights[val] += weight
            
        # Aggregate weights for items2
        for val, weight in items2:
            weights[val] += weight
            
        # Format as [[val, total_weight], ...] and sort by val
        res = [[val, weight] for val, weight in weights.items()]
        res.sort(key=lambda x: x[0])
        
        return res