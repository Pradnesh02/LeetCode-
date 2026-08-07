class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        m = len(s)
        answer = []
        
        for i in range(m):
            r, c = startPos[0], startPos[1]
            executed = 0
            
            for j in range(i, m):
                move = s[j]
                if move == 'L':
                    c -= 1
                elif move == 'R':
                    c += 1
                elif move == 'U':
                    r -= 1
                elif move == 'D':
                    r += 1
                    
                # Check if position is within grid boundaries
                if 0 <= r < n and 0 <= c < n:
                    executed += 1
                else:
                    break
                    
            answer.append(executed)
            
        return answer