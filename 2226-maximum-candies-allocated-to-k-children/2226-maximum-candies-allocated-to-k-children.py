class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        low = 1
        high = max(candies)
        ans = 0

        while low <= high:
            mid = (low + high) // 2

            # Count how many children can get `mid` candies
            count = sum(pile // mid for pile in candies)

            if count >= k:
                ans = mid
                low = mid + 1  # Try for a larger pile size
            else:
                high = mid - 1  # Reduce pile size

        return ans