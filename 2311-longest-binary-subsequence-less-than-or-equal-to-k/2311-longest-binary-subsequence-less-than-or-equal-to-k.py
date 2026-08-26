class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        curr_val = 0
        count = 0
        power = 0
        
        # Traverse from right to left (least significant to most significant)
        for ch in reversed(s):
            if ch == '0':
                count += 1
                power += 1
            else:
                # Include '1' if it keeps the formed value <= k
                if power < 60 and curr_val + (1 << power) <= k:
                    curr_val += (1 << power)
                    count += 1
                    power += 1
                    
        return count