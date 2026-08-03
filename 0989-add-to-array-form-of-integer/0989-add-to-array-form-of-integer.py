class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        i = len(num) - 1
        
        # Traverse from right to left while there are still digits in `num` or carry in `k`
        while i >= 0 and k > 0:
            k += num[i]
            num[i] = k % 10
            k //= 10
            i -= 1
            
        # If `k` still has carry digits left (e.g. adding 806 to [2, 1, 5])
        while k > 0:
            num.insert(0, k % 10)
            k //= 10
            
        return num