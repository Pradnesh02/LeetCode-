class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        # Count white blocks in the initial window of length k
        curr_whites = blocks[:k].count('W')
        min_whites = curr_whites
        
        # Slide the window across the rest of the string
        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                curr_whites -= 1
            if blocks[i] == 'W':
                curr_whites += 1
                
            min_whites = min(min_whites, curr_whites)
            
        return min_whites