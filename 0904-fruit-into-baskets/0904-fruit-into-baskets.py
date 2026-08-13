class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        basket = {}
        left = 0
        max_fruits = 0
        
        for right in range(len(fruits)):
            # Add current fruit to basket
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1
            
            # If we have more than 2 types of fruit, shrink window from left
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            
            # Update max length of valid window
            max_fruits = max(max_fruits, right - left + 1)
            
        return max_fruits