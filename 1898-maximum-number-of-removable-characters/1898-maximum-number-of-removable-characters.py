class Solution:
    def maximumRemovals(self, s: str, p: str, removable: list[int]) -> int:
        def is_subsequence(k: int) -> bool:
            removed = set(removable[:k])
            i, j = 0, 0
            while i < len(s) and j < len(p):
                if i not in removed and s[i] == p[j]:
                    j += 1
                i += 1
            return j == len(p)

        low = 0
        high = len(removable)
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if is_subsequence(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans