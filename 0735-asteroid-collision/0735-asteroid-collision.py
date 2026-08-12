class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        
        for ast in asteroids:
            # Collision happens only when stack top is moving right (> 0) 
            # and incoming ast is moving left (< 0)
            while stack and stack[-1] > 0 and ast < 0:
                diff = stack[-1] + ast
                
                if diff < 0:
                    # Top asteroid explodes, check next in stack
                    stack.pop()
                elif diff > 0:
                    # Incoming asteroid explodes, stop collision loop
                    break
                else:
                    # Both asteroids explode
                    stack.pop()
                    break
            else:
                # Executes if while loop did not break (incoming ast survived)
                stack.append(ast)
                
        return stack