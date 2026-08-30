import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            # Calculate total hours needed to eat all piles at speed `mid`
            total_hours = sum((pile + mid - 1) // mid for pile in piles)

            if total_hours <= h:
                ans = mid
                high = mid - 1  # Try a slower speed
            else:
                low = mid + 1  # Need to eat faster

        return ans