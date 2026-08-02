from collections import defaultdict

class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        box_counts = defaultdict(int)
        
        for ball in range(lowLimit, highLimit + 1):
            # Calculate the sum of digits for the current ball number
            box_num = sum(int(digit) for digit in str(ball))
            box_counts[box_num] += 1
            
        # Return the maximum number of balls in any box
        return max(box_counts.values())