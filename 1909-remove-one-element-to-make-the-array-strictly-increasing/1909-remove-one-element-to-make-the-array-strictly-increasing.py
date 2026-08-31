class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        count = 0
        
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                count += 1
                if count > 1:
                    return False
                
                # If removing nums[i - 1] doesn't fix the order with nums[i - 2],
                # we are forced to remove nums[i] instead (by updating its value to nums[i-1]).
                if i > 1 and nums[i] <= nums[i - 2]:
                    nums[i] = nums[i - 1]
                    
        return True