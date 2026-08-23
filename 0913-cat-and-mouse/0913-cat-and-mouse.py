from collections import deque

class Solution(object):
    def catMouseGame(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n = len(graph)
        MOUSE_TURN, CAT_TURN = 1, 2
        DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2
        
        # color[m][c][turn] stores outcome: 0=DRAW, 1=MOUSE_WIN, 2=CAT_WIN
        color = [[[0] * 3 for _ in range(n)] for _ in range(n)]
        
        # degree[m][c][turn] stores number of unexplored valid moves
        degree = [[[0] * 3 for _ in range(n)] for _ in range(n)]
        
        for m in range(n):
            for c in range(1, n):
                degree[m][c][MOUSE_TURN] = len(graph[m])
                degree[m][c][CAT_TURN] = len([nxt for nxt in graph[c] if nxt != 0])
                
        queue = deque()
        
        # Initialize terminal states
        for c in range(1, n):
            for turn in (1, 2):
                # Mouse reaches hole (0) -> Mouse wins
                color[0][c][turn] = MOUSE_WIN
                queue.append((0, c, turn, MOUSE_WIN))
                
                # Cat catches mouse -> Cat wins
                color[c][c][turn] = CAT_WIN
                queue.append((c, c, turn, CAT_WIN))
                
        # Find predecessor states
        def get_parents(m, c, turn):
            parents = []
            if turn == MOUSE_TURN:
                # Previous turn was CAT_TURN moving from prev_c to c
                for prev_c in graph[c]:
                    if prev_c != 0:
                        parents.append((m, prev_c, CAT_TURN))
            else:
                # Previous turn was MOUSE_TURN moving from prev_m to m
                for prev_m in graph[m]:
                    parents.append((prev_m, c, MOUSE_TURN))
            return parents

        # Retrograde BFS
        while queue:
            m, c, turn, win_res = queue.popleft()
            
            for pm, pc, pturn in get_parents(m, c, turn):
                if color[pm][pc][pturn] == DRAW:
                    # If parent player can move to a winning state for themselves
                    if (pturn == MOUSE_TURN and win_res == MOUSE_WIN) or \
                       (pturn == CAT_TURN and win_res == CAT_WIN):
                        color[pm][pc][pturn] = win_res
                        queue.append((pm, pc, pturn, win_res))
                    else:
                        # Otherwise decrement parent degree
                        degree[pm][pc][pturn] -= 1
                        if degree[pm][pc][pturn] == 0:
                            # All transitions lead to opponent winning
                            opp_win = CAT_WIN if pturn == MOUSE_TURN else MOUSE_WIN
                            color[pm][pc][pturn] = opp_win
                            queue.append((pm, pc, pturn, opp_win))
                            
        return color[1][2][MOUSE_TURN]