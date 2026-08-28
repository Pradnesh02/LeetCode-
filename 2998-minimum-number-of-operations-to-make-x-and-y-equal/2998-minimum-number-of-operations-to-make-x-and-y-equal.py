from functools import lru_cache


class Solution:

    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        @lru_cache(None)
        def solve(v: int) -> int:
            if v <= y:
                return y - v

            # Option 1: Decrement all the way from v down to y
            res = v - y

            # Option 2: Round down to the nearest multiple of 11, then divide
            res = min(res, (v % 11) + 1 + solve(v // 11))

            # Option 3: Round up to the nearest multiple of 11, then divide
            res = min(res, (11 - (v % 11)) + 1 + solve(v // 11 + 1))

            # Option 4: Round down to the nearest multiple of 5, then divide
            res = min(res, (v % 5) + 1 + solve(v // 5))

            # Option 5: Round up to the nearest multiple of 5, then divide
            res = min(res, (5 - (v % 5)) + 1 + solve(v // 5 + 1))

            return res

        return solve(x)