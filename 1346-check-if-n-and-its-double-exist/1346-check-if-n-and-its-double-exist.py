class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()

        for x in arr:
            if (2 * x in seen) or (x % 2 == 0 and x // 2 in seen):
                return True
            seen.add(x)

        return False