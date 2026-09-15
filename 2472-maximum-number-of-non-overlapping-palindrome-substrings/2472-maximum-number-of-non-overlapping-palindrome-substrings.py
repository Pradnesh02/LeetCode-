class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_end = -1  # End index of the last chosen palindrome

        # Helper to check if s[l..r] is a palindrome
        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for i in range(n):
            # Check for a valid palindrome of length k ending at or before i
            # Candidates are of length k and length k + 1
            if i - k + 1 > last_end and is_palindrome(i - k + 1, i):
                ans += 1
                last_end = i
            elif i - k > last_end and is_palindrome(i - k, i):
                ans += 1
                last_end = i

        return ans