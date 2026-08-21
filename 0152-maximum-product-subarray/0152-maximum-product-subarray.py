class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0

        res = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            
            if x < 0:
                cur_max, cur_min = cur_min, cur_max

            cur_max = max(x, cur_max * x)
            cur_min = min(x, cur_min * x)

            res = max(res, cur_max)

        return res