class Solution:

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        # Iterate up to n - 1 because when we reach n - 1, we are already at the destination
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            # When we reach the boundary of the current jump, increment jump count
            if i == current_end:
                jumps += 1
                current_end = farthest

                if current_end >= n - 1:
                    break

        return jumps