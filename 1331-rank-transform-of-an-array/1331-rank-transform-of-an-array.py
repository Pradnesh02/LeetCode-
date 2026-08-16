class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        rank_map = {}
        for rank, val in enumerate(sorted(set(arr)), 1):
            rank_map[val] = rank
            
        return [rank_map[val] for val in arr]