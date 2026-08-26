class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        remaining = n
        left_to_right = True
        
        while remaining > 1:
            # The head shifts if moving from left-to-right 
            # or if moving right-to-left with an odd count of elements
            if left_to_right or remaining % 2 == 1:
                head += step
                
            step *= 2
            remaining //= 2
            left_to_right = not left_to_right
            
        return head