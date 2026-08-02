from collections import defaultdict

class Solution(object):
    def queryResults(self, limit, queries):
        """
        :type limit: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ball_to_color = {}         # Maps ball_label -> current_color
        color_counts = defaultdict(int)  # Maps color -> number_of_balls_with_this_color
        
        result = []
        
        for ball, new_color in queries:
            # If the ball already has a color, update its previous color count
            if ball in ball_to_color:
                old_color = ball_to_color[ball]
                color_counts[old_color] -= 1
                if color_counts[old_color] == 0:
                    del color_counts[old_color]  # Remove color if no balls use it anymore
            
            # Assign the new color to the ball
            ball_to_color[ball] = new_color
            color_counts[new_color] += 1
            
            # Number of distinct active colors is the number of keys in color_counts
            result.append(len(color_counts))
            
        return result