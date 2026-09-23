class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)
        
        # If the sum of all elements equals x, we take the entire array
        if target == 0:
            return n
        # If target is negative, sum(nums) < x, impossible to reach x
        if target < 0:
            return -1
        
        left = 0
        current_sum = 0
        max_len = -1
        
        for right in range(n):
            current_sum += nums[right]
            
            # Shrink window from the left while sum exceeds target
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            if current_sum == target:
                max_len = max(max_len, right - left + 1)
                
        return n - max_len if max_len != -1 else -1