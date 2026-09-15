class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        path = []

        def backtrack(start: int):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):
                sub = s[start:end]
                # Check if the current substring is a palindrome
                if sub == sub[::-1]:
                    path.append(sub)
                    backtrack(end)
                    path.pop()

        backtrack(0)
        return res