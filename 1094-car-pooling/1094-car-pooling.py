class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        # Array to store passenger delta at each coordinate (locations <= 1000)
        passenger_change = [0] * 1001
        
        for num_passengers, start, end in trips:
            passenger_change[start] += num_passengers
            passenger_change[end] -= num_passengers
            
        current_passengers = 0
        for change in passenger_change:
            current_passengers += change
            if current_passengers > capacity:
                return False
                
        return True