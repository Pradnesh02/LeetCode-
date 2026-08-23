class Solution(object):
    def canMouseWin(self, grid, catJump, mouseJump):
        """
        :type grid: List[str]
        :type catJump: int
        :type mouseJump: int
        :rtype: bool
        """
        rows, cols = len(grid), len(grid[0])
        
        # Locate positions and count available floor cells
        available = 0
        mouse_start = cat_start = food = None
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '#':
                    available += 1
                if grid[r][c] == 'M':
                    mouse_start = (r, c)
                elif grid[r][c] == 'C':
                    cat_start = (r, c)
                elif grid[r][c] == 'F':
                    food = (r, c)
                    
        # MAX_TURNS: If turns exceed 2 * available floor cells, Cat wins
        MAX_TURNS = 2 * available
        memo = {}
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(turn, mouse_pos, cat_pos):
            # Base conditions
            if turn >= MAX_TURNS:
                return False  # Cat wins (Mouse loses)
            if mouse_pos == cat_pos:
                return False  # Cat caught Mouse
            if cat_pos == food:
                return False  # Cat reached Food
            if mouse_pos == food:
                return True   # Mouse reached Food
                
            state = (turn, mouse_pos, cat_pos)
            if state in memo:
                return memo[state]
                
            is_mouse_turn = (turn % 2 == 0)
            
            if is_mouse_turn:
                # Mouse tries to find ANY move that leads to a win (True)
                mr, mc = mouse_pos
                # Option to stay in the same place
                if dfs(turn + 1, mouse_pos, cat_pos):
                    memo[state] = True
                    return True
                
                # Jump in all 4 directions up to mouseJump
                for dr, dc in directions:
                    for jump in range(1, mouseJump + 1):
                        nr, nc = mr + dr * jump, mc + dc * jump
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                            if dfs(turn + 1, (nr, nc), cat_pos):
                                memo[state] = True
                                return True
                        else:
                            break  # Hit wall or boundary, cannot jump further in this direction
                            
                memo[state] = False
                return False
                
            else:
                # Cat tries to find ANY move that leads to Cat's win (Mouse result False)
                cr, cc = cat_pos
                # Option to stay in the same place
                if not dfs(turn + 1, mouse_pos, cat_pos):
                    memo[state] = False
                    return False
                
                # Jump in all 4 directions up to catJump
                for dr, dc in directions:
                    for jump in range(1, catJump + 1):
                        nr, nc = cr + dr * jump, cc + dc * jump
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                            if not dfs(turn + 1, mouse_pos, (nr, nc)):
                                memo[state] = False
                                return False
                        else:
                            break
                            
                memo[state] = True
                return True

        return dfs(0, mouse_start, cat_start)