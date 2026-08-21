class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        def is_arithmetic(sub):
            sub.sort()
            diff = sub[1] - sub[0]
            for i in range(2, len(sub)):
                if sub[i] - sub[i - 1] != diff:
                    return False
            return True

        result = []
        for left, right in zip(l, r):
            sub = nums[left : right + 1]
            result.append(is_arithmetic(sub))

        return result