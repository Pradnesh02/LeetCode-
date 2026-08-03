class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        n = len(aliceValues)
        
        # Combine the values of both players for each stone
        # Priority for choosing stone i is (aliceValues[i] + bobValues[i])
        stones = [(aliceValues[i] + bobValues[i], aliceValues[i], bobValues[i]) for i in range(n)]
        
        # Sort stones in descending order of their combined values
        stones.sort(key=lambda x: x[0], reverse=True)
        
        alice_score = 0
        bob_score = 0
        
        # Alternate turns: Alice picks on even indices, Bob on odd indices
        for i in range(n):
            if i % 2 == 0:
                alice_score += stones[i][1]  # Alice gets aliceValues
            else:
                bob_score += stones[i][2]    # Bob gets bobValues
                
        if alice_score > bob_score:
            return 1
        elif bob_score > alice_score:
            return -1
        else:
            return 0