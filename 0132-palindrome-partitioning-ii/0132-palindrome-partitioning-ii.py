class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # dp[i] stores the minimum cuts needed for s[0..i]
        # Initialize with maximum cuts: i cuts for length i + 1
        dp = list(range(n))

        for mid in range(n):
            # Odd-length palindromes centered at mid
            l, r = mid, mid
            while l >= 0 and r < n and s[l] == s[r]:
                cuts = 0 if l == 0 else dp[l - 1] + 1
                if cuts < dp[r]:
                    dp[r] = cuts
                l -= 1
                r += 1

            # Even-length palindromes centered between mid and mid + 1
            l, r = mid, mid + 1
            while l >= 0 and r < n and s[l] == s[r]:
                cuts = 0 if l == 0 else dp[l - 1] + 1
                if cuts < dp[r]:
                    dp[r] = cuts
                l -= 1
                r += 1

        return dp[-1]