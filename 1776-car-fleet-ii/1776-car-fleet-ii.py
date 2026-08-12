class Solution(object):
    def getCollisionTimes(self, cars):
        """
        :type cars: List[List[int]]
        :rtype: List[float]
        """
        n = len(cars)
        ans = [-1.0] * n
        stack = []  # Stores indices of cars ahead
        
        for i in range(n - 1, -1, -1):
            p1, s1 = cars[i]
            
            while stack:
                j = stack[-1]
                p2, s2 = cars[j]
                
                # Case 1: Car i is slower or equal speed -> can never catch car j
                # Case 2: Car i catches car j after car j has already merged with a fleet ahead
                if s1 <= s2 or (ans[j] > 0 and (float(p2 - p1) / (s1 - s2)) >= ans[j]):
                    stack.pop()
                else:
                    break
                    
            if stack:
                j = stack[-1]
                p2, s2 = cars[j]
                ans[i] = float(p2 - p1) / (s1 - s2)
                
            stack.append(i)
            
        return ans