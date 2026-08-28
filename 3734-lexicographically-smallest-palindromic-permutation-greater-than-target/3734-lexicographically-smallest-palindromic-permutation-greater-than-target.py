from collections import Counter


class Solution:

    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_counts = Counter(s)

        # Step 1: Validate if a palindrome can be formed
        odd_chars = [c for c, count in total_counts.items() if count % 2 != 0]
        if len(odd_chars) > 1 or (n % 2 == 0 and len(odd_chars) > 0):
            return ""

        mid_char = odd_chars[0] if odd_chars else ""
        half_counts = Counter({c: total_counts[c] // 2 for c in total_counts})
        m = n // 2

        # Step 2: Check if exact match of first half yields a valid palindrome > target
        exact_valid = True
        curr_half = half_counts.copy()
        for i in range(m):
            c = target[i]
            if curr_half[c] > 0:
                curr_half[c] -= 1
            else:
                exact_valid = False
                break

        if exact_valid:
            first_half = target[:m]
            cand = first_half + mid_char + first_half[::-1]
            if cand > target:
                return cand

        # Step 3: Find the longest common prefix where we can increment a character
        # Track prefix character counts to know available characters at each position
        prefix_counts = Counter()
        prefix_valid = [True] * (m + 1)
        temp_counts = half_counts.copy()

        for i in range(m):
            c = target[i]
            if temp_counts[c] > 0:
                temp_counts[c] -= 1
            else:
                for j in range(i + 1, m + 1):
                    prefix_valid[j] = False
                break

        for i in range(m - 1, -1, -1):
            if not prefix_valid[i]:
                continue

            # Available counts after matching target[:i]
            avail = half_counts.copy()
            for j in range(i):
                avail[target[j]] -= 1

            # Try to place the smallest character strictly greater than target[i]
            target_char = target[i]
            chosen_char = None
            for c in sorted(avail.keys()):
                if c > target_char and avail[c] > 0:
                    chosen_char = c
                    break

            if chosen_char is not None:
                avail[chosen_char] -= 1
                # Build the remainder of the first half using smallest available characters
                rest = []
                for c in sorted(avail.keys()):
                    rest.extend([c] * avail[c])

                first_half = target[:i] + chosen_char + "".join(rest)
                return first_half + mid_char + first_half[::-1]

        return ""