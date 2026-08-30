class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        low = 1
        high = max(quantities)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            # Calculate total stores required if each store can take at most `mid` items
            stores_needed = sum((q + mid - 1) // mid for q in quantities)

            if stores_needed <= n:
                ans = mid
                high = mid - 1  # Try a smaller maximum
            else:
                low = mid + 1  # Need a larger maximum

        return ans