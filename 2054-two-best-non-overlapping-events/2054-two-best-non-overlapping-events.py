from bisect import bisect_right
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Sort events by start time
        events.sort(key=lambda x: x[0])
        n = len(events)
        
        # suffix_max[i] stores the max value from events[i:]
        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(events[i][2], suffix_max[i + 1])
            
        start_times = [event[0] for event in events]
        max_sum = 0
        
        for start, end, val in events:
            # Option 1: Attend only this event
            current_sum = val
            
            # Option 2: Attend this event and the best valid next event
            # Find the first event with start_time > end
            next_idx = bisect_right(start_times, end)
            if next_idx < n:
                current_sum += suffix_max[next_idx]
                
            max_sum = max(max_sum, current_sum)
            
        return max_sum