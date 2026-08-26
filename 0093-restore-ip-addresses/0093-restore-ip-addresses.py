from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)
        
        # An IP address must have between 4 and 12 digits
        if n < 4 or n > 12:
            return res
        
        def backtrack(start: int, parts: List[str]):
            # If we have 4 segments and reached the end of s, it's a valid IP
            if len(parts) == 4:
                if start == n:
                    res.append(".".join(parts))
                return
            
            # Prune search space: remaining characters cannot fit in remaining slots
            remaining_slots = 4 - len(parts)
            remaining_chars = n - start
            if not (remaining_slots <= remaining_chars <= remaining_slots * 3):
                return
            
            # Try segment lengths from 1 to 3
            for length in range(1, 4):
                if start + length > n:
                    break
                
                segment = s[start:start + length]
                
                # Check for leading zero or value > 255
                if (length > 1 and segment[0] == '0') or int(segment) > 255:
                    continue
                
                backtrack(start + length, parts + [segment])
        
        backtrack(0, [])
        return res