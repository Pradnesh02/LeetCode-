class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        current_sum = 0
        # Map stores frequency of prefix sums encountered
        # Initialize with 0: 1 to account for subarrays starting at index 0
        prefix_sums = {0: 1}
        
        for num in nums:
            current_sum += num
            
            # Check if there exists a prefix sum such that current_sum - prefix_sum = k
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]
                
            # Record current prefix sum in the hash map
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return count