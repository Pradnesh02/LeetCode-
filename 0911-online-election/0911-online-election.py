import bisect
from collections import defaultdict

class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.times = times
        self.leaders = []
        
        vote_counts = defaultdict(int)
        leader = None
        max_votes = 0
        
        for p in persons:
            vote_counts[p] += 1
            # Update leader if current candidate has >= max votes (tie goes to most recent)
            if vote_counts[p] >= max_votes:
                leader = p
                max_votes = vote_counts[p]
            self.leaders.append(leader)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        # Find the rightmost index where times[i] <= t
        idx = bisect.bisect_right(self.times, t) - 1
        return self.leaders[idx]