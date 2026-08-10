class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        target = 10
        alice_turn = True
        
        while n >= target:
            n -= target
            target -= 1
            alice_turn = not alice_turn
            
        # If the loop breaks on Alice's turn, it means Alice couldn't make a move, 
        # so Bob wins (return False). If it breaks on Bob's turn, Alice wins (return True).
        return not alice_turn