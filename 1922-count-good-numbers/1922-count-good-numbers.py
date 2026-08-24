class Solution(object):
    def countGoodNumbers(self, n):
        MOD = 10**9 + 7
        
        even_pos = (n + 1) // 2
        odd_pos = n // 2
        
        # Modular exponentiation: pow(base, exp, mod)
        ans = (pow(5, even_pos, MOD) * pow(4, odd_pos, MOD)) % MOD
        return ans