from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()
        
        # Populate the queues with senator indices
        for i, ch in enumerate(senate):
            if ch == 'R':
                radiant.append(i)
            else:
                dire.append(i)
                
        # Simulate the voting process
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            
            # The senator with the earlier turn bans the opposing senator
            # and moves to the end of the line for the next round
            if r_idx < d_idx:
                radiant.append(r_idx + n)
            else:
                dire.append(d_idx + n)
                
        return "Radiant" if radiant else "Dire"