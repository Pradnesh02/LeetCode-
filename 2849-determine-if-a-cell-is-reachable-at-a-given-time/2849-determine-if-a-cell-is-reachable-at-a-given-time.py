class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # Minimum time needed to reach (fx, fy) using 8-directional movement (Chebyshev distance)
        min_time = max(abs(sx - fx), abs(sy - fy))
        
        # Special edge case: start and finish are the same cell
        # In 1 second, you must move away to an adjacent cell and cannot immediately return
        if min_time == 0:
            return t != 1
            
        return t >= min_time