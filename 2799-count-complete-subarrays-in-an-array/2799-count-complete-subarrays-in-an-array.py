from collections import defaultdict
from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_distinct = len(set(nums))
        freq = defaultdict(int)
        
        n = len(nums)
        left = 0
        ans = 0
        
        for right in range(n):
            freq[nums[right]] += 1
            
            # When the window contains all distinct elements
            while len(freq) == total_distinct:
                # All subarrays starting at 'left' and ending at indices >= 'right' are valid
                ans += (n - right)
                
                # Shrink window from the left
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
                
        return ans