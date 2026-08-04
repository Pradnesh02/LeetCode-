class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        window_size = n - k
        total_sum = sum(cardPoints)
        
        if window_size == 0:
            return total_sum
            
        # Sum of the first window of length (n - k)
        curr_window_sum = sum(cardPoints[:window_size])
        min_window_sum = curr_window_sum
        
        # Slide the window of length (n - k)
        for i in range(window_size, n):
            curr_window_sum += cardPoints[i] - cardPoints[i - window_size]
            min_window_sum = min(min_window_sum, curr_window_sum)
            
        return total_sum - min_window_sum