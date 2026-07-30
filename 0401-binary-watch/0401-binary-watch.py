class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        res = []
        
        # Iterate over all possible hours (0-11) and minutes (0-59)
        for h in range(12):
            for m in range(60):
                # Count the total number of set bits (1s) in both hour and minute binary representations
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    # Format minute with leading zero if needed (e.g., "4:05")
                    res.append("{}:{:02d}".format(h, m))
                    
        return res