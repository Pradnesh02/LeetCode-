from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0 or indexDiff <= 0:
            return False
        
        # Bucket size is valueDiff + 1 so any two values in the same bucket satisfy the condition
        bucket_size = valueDiff + 1
        buckets = {}
        
        for i, num in enumerate(nums):
            # Compute the bucket ID for the current number
            bucket_id = num // bucket_size
            
            # Check if current bucket already contains a number
            if bucket_id in buckets:
                return True
            
            # Check left adjacent bucket
            if (bucket_id - 1 in buckets) and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
            
            # Check right adjacent bucket
            if (bucket_id + 1 in buckets) and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
            
            # Add current number to bucket
            buckets[bucket_id] = num
            
            # Remove elements outside the sliding window of size indexDiff
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // bucket_size]
                
        return False