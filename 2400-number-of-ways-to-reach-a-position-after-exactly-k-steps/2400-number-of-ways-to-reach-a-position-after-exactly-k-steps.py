import math

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10**9 + 7
        dist = abs(startPos - endPos)
        
        # If distance exceeds steps or parities don't match, target is unreachable
        if dist > k or (k - dist) % 2 != 0:
            return 0
        
        # Let r be the number of right steps: r = (k + dist) // 2
        r = (k + dist) // 2
        
        # Result is combination C(k, r) mod 10^9 + 7
        return math.comb(k, r) % MOD