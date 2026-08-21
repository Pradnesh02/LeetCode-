class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        
        def count_less_equal(mid):
            count = 0
            r = n - 1
            c = 0
            while r >= 0 and c < n:
                if matrix[r][c] <= mid:
                    count += (r + 1)
                    c += 1
                else:
                    r -= 1
            return count

        left = matrix[0][0]
        right = matrix[n - 1][n - 1]

        while left < right:
            mid = (left + right) // 2
            if count_less_equal(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left