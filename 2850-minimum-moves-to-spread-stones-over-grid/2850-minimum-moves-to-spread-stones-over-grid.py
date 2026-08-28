from itertools import permutations


class Solution:

    def minimumMoves(self, grid: List[List[int]]) -> int:
        zeros = []
        extras = []

        # Identify cells with 0 stones and cells with extra stones
        for r in range(3):
            for c in range(3):
                if grid[r][c] == 0:
                    zeros.append((r, c))
                elif grid[r][c] > 1:
                    # Append each excess stone individually
                    extras.extend([(r, c)] * (grid[r][c] - 1))

        if not zeros:
            return 0

        min_moves = float("inf")

        # Try all possible pairings of extra stones to empty cells
        for p in set(permutations(extras)):
            current_moves = sum(
                abs(z[0] - e[0]) + abs(z[1] - e[1]) for z, e in zip(zeros, p)
            )
            min_moves = min(min_moves, current_moves)

        return min_moves