class Solution(object):
    def getDescentPeriods(self, prices):
        if not prices:
            return 0

        total = 1
        streak = 1

        for i in range(1, len(prices)):
            if prices[i - 1] - prices[i] == 1:
                streak += 1
            else:
                streak = 1
            total += streak

        return total