class Solution(object):
    def wonderfulSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        # Frequency of prefix masks seen so far (10 bits = 1024 total possible states)
        count = [0] * 1024
        count[0] = 1  # Base case for prefix with 0 mask
        
        mask = 0
        ans = 0
        
        for char in word:
            # Toggle the bit corresponding to current character ('a' -> 0, 'b' -> 1, ..., 'j' -> 9)
            bit = ord(char) - ord('a')
            mask ^= (1 << bit)
            
            # Case 1: All characters in substring have even counts (mask matches previous mask exactly)
            ans += count[mask]
            
            # Case 2: Exactly one character has an odd count (mask differs by 1 bit)
            for i in range(10):
                ans += count[mask ^ (1 << i)]
                
            # Store current prefix mask occurrence
            count[mask] += 1
            
        return ans