from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n

        # Helper function to convert 1D square index (1 to n^2) to (row, col)
        def get_coordinates(square: int) -> tuple[int, int]:
            # Distance from the bottom row (0-indexed from bottom)
            row_from_bottom = (square - 1) // n
            r = n - 1 - row_from_bottom
            
            col_offset = (square - 1) % n
            # If row_from_bottom is even, movement is left-to-right
            # If row_from_bottom is odd, movement is right-to-left
            if row_from_bottom % 2 == 0:
                c = col_offset
            else:
                c = n - 1 - col_offset
                
            return r, c

        queue = deque([(1, 0)])  # (current_square, moves)
        visited = {1}

        while queue:
            curr, moves = queue.popleft()

            if curr == target:
                return moves

            # Try all standard 6-sided die rolls
            for roll in range(1, 7):
                nxt = curr + roll
                if nxt > target:
                    break

                r, c = get_coordinates(nxt)
                # Check if there is a snake or ladder
                dest = board[r][c] if board[r][c] != -1 else nxt

                if dest not in visited:
                    visited.add(dest)
                    queue.append((dest, moves + 1))

        return -1