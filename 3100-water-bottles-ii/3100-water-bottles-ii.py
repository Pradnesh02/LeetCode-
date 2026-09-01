class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        # Drink all initially available full bottles
        total_drunk = numBottles
        empty_bottles = numBottles
        
        # Continue exchanging whenever we have enough empty bottles
        while empty_bottles >= numExchange:
            empty_bottles -= numExchange
            numExchange += 1
            
            # Drink the newly exchanged full bottle
            total_drunk += 1
            empty_bottles += 1
            
        return total_drunk