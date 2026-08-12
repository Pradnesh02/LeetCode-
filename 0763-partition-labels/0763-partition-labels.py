class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        # Store the last occurrence index of each character
        last = {char: i for i, char in enumerate(s)}
        
        result = []
        size = 0
        end = 0
        
        for i, char in enumerate(s):
            size += 1
            end = max(end, last[char])
            
            # Reached the end of the current partition
            if i == end:
                result.append(size)
                size = 0
                
        return result