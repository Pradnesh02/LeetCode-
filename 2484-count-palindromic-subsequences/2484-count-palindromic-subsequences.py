class Solution(object):
    def countPalindromes(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        n = len(s)
        
        if n < 5:
            return 0
            
        # pref[i][d1][d2] stores frequency of pattern (d1, d2) in s[0..i]
        pref = [[[0] * 10 for _ in range(10)] for _ in range(n)]
        # suff[i][d1][d2] stores frequency of pattern (d1, d2) in s[i..n-1]
        suff = [[[0] * 10 for _ in range(10)] for _ in range(n)]
        
        # Precompute prefixes
        cnt = [0] * 10
        for i in range(n):
            d = int(s[i])
            if i > 0:
                for d1 in range(10):
                    for d2 in range(10):
                        pref[i][d1][d2] = pref[i - 1][d1][d2]
                for d1 in range(10):
                    pref[i][d1][d] += cnt[d1]
            cnt[d] += 1
            
        # Precompute suffixes
        cnt = [0] * 10
        for i in range(n - 1, -1, -1):
            d = int(s[i])
            if i < n - 1:
                for d1 in range(10):
                    for d2 in range(10):
                        suff[i][d1][d2] = suff[i + 1][d1][d2]
                for d2 in range(10):
                    suff[i][d][d2] += cnt[d2]
            cnt[d] += 1
            
        total = 0
        
        # Iterate over all possible center indices for length 5 palindrome
        for i in range(2, n - 2):
            for d1 in range(10):
                for d2 in range(10):
                    # Pattern on left is d1 d2, matching pattern on right is d2 d1
                    left_count = pref[i - 1][d1][d2]
                    right_count = suff[i + 1][d2][d1]
                    total = (total + left_count * right_count) % MOD
                    
        return total