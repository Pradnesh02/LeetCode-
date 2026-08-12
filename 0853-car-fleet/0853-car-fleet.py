class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        # Pair positions with speeds and sort in descending order of position
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        current_max_time = 0.0
        
        for pos, spd in cars:
            time = float(target - pos) / spd
            
            # If a car takes longer than the fleet ahead, it becomes a new fleet leader
            if time > current_max_time:
                fleets += 1
                current_max_time = time
                
        return fleets