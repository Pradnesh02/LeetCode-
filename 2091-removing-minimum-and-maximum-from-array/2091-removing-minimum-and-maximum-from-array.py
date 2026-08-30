class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        # Find the 0-indexed positions of the min and max elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        # Order indices so low <= high
        low = min(min_idx, max_idx)
        high = max(min_idx, max_idx)

        # 3 possible deletion strategies:
        # 1. Remove both from the front (left)
        from_front = high + 1

        # 2. Remove both from the back (right)
        from_back = n - low

        # 3. Remove one from the front and one from the back
        from_both_ends = (low + 1) + (n - high)

        return min(from_front, from_back, from_both_ends)