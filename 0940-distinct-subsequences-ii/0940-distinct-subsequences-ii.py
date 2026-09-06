class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        # ends[i] records the count of distinct subsequences ending with character chr(ord('a') + i)
        ends = [0] * 26
        
        for ch in s:
            idx = ord(ch) - ord('a')
            # 1 (for ch itself) + sum of all distinct subsequences formed so far
            ends[idx] = (sum(ends) + 1) % MOD
            
        return sum(ends) % MOD