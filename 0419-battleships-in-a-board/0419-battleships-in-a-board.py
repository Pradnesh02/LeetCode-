class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if not board or not board[0]:
            return 0

        m, n = len(board), len(board[0])
        count = 0

        for r in range(m):
            for c in range(n):
                # If the cell is an 'X', check if it is the "head" (top-leftmost cell) of a battleship
                if board[r][c] == 'X':
                    # If there's an 'X' directly above it, it's part of an existing vertical battleship
                    if r > 0 and board[r - 1][c] == 'X':
                        continue
                    # If there's an 'X' directly to its left, it's part of an existing horizontal battleship
                    if c > 0 and board[r][c - 1] == 'X':
                        continue
                    
                    # Otherwise, this 'X' marks the top/left end of a new battleship
                    count += 1

        return count