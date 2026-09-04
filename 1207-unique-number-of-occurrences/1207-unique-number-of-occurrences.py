from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = Counter(arr).values()
        return len(freq) == len(set(freq))