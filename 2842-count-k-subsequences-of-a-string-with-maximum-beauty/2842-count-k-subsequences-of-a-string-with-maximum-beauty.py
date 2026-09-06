import math
from collections import Counter

class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        counts = Counter(s)
        
        # If there are fewer than k unique characters, impossible
        if len(counts) < k:
            return 0
            
        freqs = sorted(counts.values(), reverse=True)
        target = freqs[k - 1]
        
        # Count available characters with frequency == target
        m = freqs.count(target)
        
        ans = 1
        need = 0
        
        for f in freqs[:k]:
            if f > target:
                ans = (ans * f) % MOD
            else:
                need += 1
                
        # Ways to choose `need` characters from `m` candidates
        comb = math.comb(m, need) % MOD
        
        # Each chosen character with frequency `target` provides `target` options
        ans = (ans * comb) % MOD
        ans = (ans * pow(target, need, MOD)) % MOD
        
        return ans