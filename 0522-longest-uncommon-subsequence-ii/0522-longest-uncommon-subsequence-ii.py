from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubsequence(s1: str, s2: str) -> bool:
            i = 0
            for char in s2:
                if i < len(s1) and s1[i] == char:
                    i += 1
            return i == len(s1)

        # Sort strings by descending length
        strs.sort(key=len, reverse=True)
        n = len(strs)

        for i in range(n):
            is_uncommon = True
            for j in range(n):
                if i != j and isSubsequence(strs[i], strs[j]):
                    is_uncommon = False
                    break
            
            if is_uncommon:
                return len(strs[i])

        return -1