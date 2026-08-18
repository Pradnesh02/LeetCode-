from collections import Counter

class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        subarray_counts = Counter()
        n = len(nums)
        
        # Iterate over all contiguous subarrays of size k
        for i in range(n - k + 1):
            unique_elements = set(nums[i:i + k])
            for val in unique_elements:
                subarray_counts[val] += 1
                
        # Find candidates that appear in exactly 1 subarray
        candidates = [val for val, count in subarray_counts.items() if count == 1]
        
        return max(candidates) if candidates else -1