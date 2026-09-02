from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        # most_common(k) returns the k elements with the highest frequencies
        return [item for item, freq in count.most_common(k)]