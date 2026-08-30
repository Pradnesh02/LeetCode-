from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        k = n // 4
        counts = Counter(s)

        # If already balanced
        if all(counts[char] <= k for char in "QWER"):
            return 0

        min_len = n
        left = 0

        # Sliding window representing the substring to replace
        for right in range(n):
            counts[s[right]] -= 1

            # While characters outside the window all appear at most k times
            while left < n and all(counts[char] <= k for char in "QWER"):
                min_len = min(min_len, right - left + 1)
                counts[s[left]] += 1
                left += 1

        return min_len