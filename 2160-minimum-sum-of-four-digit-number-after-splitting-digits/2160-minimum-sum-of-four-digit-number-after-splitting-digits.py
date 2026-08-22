class Solution(object):
    def minimumSum(self, num):
        digits = sorted(int(d) for d in str(num))
        return 10 * (digits[0] + digits[1]) + digits[2] + digits[3]