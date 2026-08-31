import random
from collections import defaultdict

class Solution:

    def __init__(self, nums: List[int]):
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        # Choose a random index directly in O(1) time
        return random.choice(self.indices[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)