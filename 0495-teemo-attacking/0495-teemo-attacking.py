class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries or duration == 0:
            return 0
            
        total_time = 0
        
        for i in range(len(timeSeries) - 1):
            # Add the minimum between actual gap and full duration
            gap = timeSeries[i + 1] - timeSeries[i]
            total_time += min(gap, duration)
            
        # Add duration for the last attack
        total_time += duration
        
        return total_time