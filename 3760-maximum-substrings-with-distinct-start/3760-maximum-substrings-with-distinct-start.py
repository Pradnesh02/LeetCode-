class Solution:
    def maxDistinct(self, s: str) -> int:
        # The number of substrings cannot exceed the number of unique characters in s.
        # We can always achieve this maximum by splitting immediately before the 
        # first occurrence of each unique character.
        return len(set(s))