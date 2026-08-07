class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        """
        :type moves: str
        :rtype: int
        """
        l_count = moves.count('L')
        r_count = moves.count('R')
        blank_count = moves.count('_')
        
        return abs(r_count - l_count) + blank_count