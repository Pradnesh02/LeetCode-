class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = -1
        max2 = -1
        max_idx = -1

        for i, num in enumerate(nums):
            if num > max1:
                max2 = max1
                max1 = num
                max_idx = i
            elif num > max2:
                max2 = num

        return max_idx if max1 >= 2 * max2 else -1