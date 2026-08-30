class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            # Compute sum of ceil(num / mid)
            total = sum((num + mid - 1) // mid for num in nums)

            if total <= threshold:
                ans = mid
                high = mid - 1  # Try a smaller divisor
            else:
                low = mid + 1  # Need a larger divisor to reduce the sum

        return ans