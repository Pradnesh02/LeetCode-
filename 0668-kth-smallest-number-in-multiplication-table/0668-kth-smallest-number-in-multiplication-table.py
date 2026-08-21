class Solution(object):
    def findKthNumber(self, m, n, k):
        def count_less_equal(mid):
            count = 0
            for i in range(1, m + 1):
                count += min(n, mid // i)
            return count

        left = 1
        right = m * n

        while left < right:
            mid = (left + right) // 2
            if count_less_equal(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left