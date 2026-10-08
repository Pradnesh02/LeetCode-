class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        for i, char in enumerate(s):
            if char == ' ':
                k -= 1
                if k == 0:
                    return s[:i]
        return s