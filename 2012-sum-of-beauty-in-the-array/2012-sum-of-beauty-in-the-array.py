class Solution(object):
    def sumOfBeauties(self, nums):
        n = len(nums)
        
        # min_right[i] stores the minimum value in nums[i:]
        min_right = [0] * n
        min_right[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            min_right[i] = min(nums[i], min_right[i + 1])
            
        total_beauty = 0
        max_left = nums[0]
        
        for i in range(1, n - 1):
            if max_left < nums[i] < min_right[i + 1]:
                total_beauty += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                total_beauty += 1
                
            max_left = max(max_left, nums[i])
            
        return total_beauty