class Solution(object):
    def bestTower(self, towers, center, radius):
        """
        :type towers: List[List[int]]
        :type center: List[int]
        :type radius: int
        :rtype: List[int]
        """
        cx, cy = center
        best_quality = -1
        best_coords = [-1, -1]
        
        for x, y, q in towers:
            # Calculate Manhattan Distance
            dist = abs(x - cx) + abs(y - cy)
            
            if dist <= radius:
                # Compare against the current best tower
                # We want higher quality, or tie-break with lexicographically smaller (x, y)
                if (q > best_quality or 
                   (q == best_quality and (x < best_coords[0] or (x == best_coords[0] and y < best_coords[1])))):
                    best_quality = q
                    best_coords = [x, y]
                    
        return best_coords