from collections import defaultdict, Counter

class Solution(object):
    def winningPlayerCount(self, n, pick):
        """
        :type n: int
        :type pick: List[List[int]]
        :rtype: int
        """
        # Map each player to a frequency counter of their picked ball colors
        player_picks = defaultdict(Counter)
        
        for player, color in pick:
            player_picks[player][color] += 1
            
        winning_players = 0
        
        # Check winning condition for each player from 0 to n - 1
        for i in range(n):
            # Player i wins if they have at least i + 1 balls of any single color
            if any(count > i for count in player_picks[i].values()):
                winning_players += 1
                
        return winning_players