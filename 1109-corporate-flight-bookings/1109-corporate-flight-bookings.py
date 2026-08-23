class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        res = [0] * n
        
        # Apply difference array updates
        for first, last, seats in bookings:
            res[first - 1] += seats
            if last < n:
                res[last] -= seats
                
        # Accumulate prefix sums
        for i in range(1, n):
            res[i] += res[i - 1]
            
        return res