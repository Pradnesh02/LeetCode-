class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Find the point in the rectangle closest to the circle's center
        nearest_x = max(x1, min(xCenter, x2))
        nearest_y = max(y1, min(yCenter, y2))
        
        # Calculate squared Euclidean distance from the circle center to this point
        dx = nearest_x - xCenter
        dy = nearest_y - yCenter
        
        return dx * dx + dy * dy <= radius * radius