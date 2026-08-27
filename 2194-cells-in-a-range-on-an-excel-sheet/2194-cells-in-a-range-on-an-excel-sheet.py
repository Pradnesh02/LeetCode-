from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        c1, r1, _, c2, r2 = s[0], int(s[1]), s[2], s[3], int(s[4])
        result = []
        
        for col_code in range(ord(c1), ord(c2) + 1):
            col_char = chr(col_code)
            for row in range(r1, r2 + 1):
                result.append(f"{col_char}{row}")
                
        return result