from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        
        for i, num in enumerate(nums):
            # Check if num was seen before within distance k
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
            
        return False