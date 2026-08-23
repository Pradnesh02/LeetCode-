class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        n = len(pref)
        arr = [pref[0]] * n
        
        for i in range(1, n):
            arr[i] = pref[i] ^ pref[i - 1]
            
        return arr