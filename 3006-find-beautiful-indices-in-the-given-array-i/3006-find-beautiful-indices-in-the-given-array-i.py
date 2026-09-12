from bisect import bisect_left
from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        len_a = len(a)
        len_b = len(b)
        
        # Collect all start indices for string a
        indices_a = [i for i in range(n - len_a + 1) if s[i:i + len_a] == a]
        
        # Collect all start indices for string b
        indices_b = [j for j in range(n - len_b + 1) if s[j:j + len_b] == b]
        
        if not indices_a or not indices_b:
            return []
        
        ans = []
        m = len(indices_b)
        
        for i in indices_a:
            pos = bisect_left(indices_b, i)
            
            # Check the closest element >= i
            if pos < m and indices_b[pos] - i <= k:
                ans.append(i)
            # Check the closest element < i
            elif pos > 0 and i - indices_b[pos - 1] <= k:
                ans.append(i)
                
        return ans