class Solution(object):
    def rankTeams(self, votes):
        """
        :type votes: List[str]
        :rtype: str
        """
        num_teams = len(votes[0])
        
        # Initialize a vote count list of size num_teams for each team
        vote_counts = {team: [0] * num_teams for team in votes[0]}
        
        # Tally the votes for each position
        for vote in votes:
            for rank, team in enumerate(vote):
                vote_counts[team][rank] += 1
                
        # Sort teams:
        # 1. Negate the vote count array for descending frequency comparison
        # 2. Team character itself for ascending alphabetical tie-breaking
        teams = list(votes[0])
        teams.sort(key=lambda team: ([-count for count in vote_counts[team]], team))
        
        return "".join(teams)