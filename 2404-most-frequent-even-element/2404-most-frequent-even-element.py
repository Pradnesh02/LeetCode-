from collections import Counter
from typing import List

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = Counter(x for x in nums if x % 2 == 0)
        
        if not counts:
            return -1
        
        # Maximize frequency (-count), minimize element value (num)
        return min(counts.keys(), key=lambda x: (-counts[x], x))