class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        tx, ty = target
        my_dist = abs(tx) + abs(ty)
        
        for gx, gy in ghosts:
            ghost_dist = abs(gx - tx) + abs(gy - ty)
            if ghost_dist <= my_dist:
                return False
                
        return True