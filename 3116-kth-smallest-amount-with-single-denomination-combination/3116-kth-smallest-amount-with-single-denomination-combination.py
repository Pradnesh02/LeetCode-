from itertools import combinations
from fractions import gcd

class Solution(object):
    def findKthSmallest(self, coins, k):
        def lcm(a, b):
            return (a * b) // gcd(a, b)

        subsets_lcm = []
        n = len(coins)

        for r in range(1, n + 1):
            sign = 1 if r % 2 == 1 else -1
            for combo in combinations(coins, r):
                curr_lcm = combo[0]
                for c in combo[1:]:
                    curr_lcm = lcm(curr_lcm, c)
                subsets_lcm.append((curr_lcm, sign))

        def count(mid):
            total = 0
            for l, sign in subsets_lcm:
                total += sign * (mid // l)
            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left