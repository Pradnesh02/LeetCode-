from collections import defaultdict

class FrequencyTracker:

    def __init__(self):
        self.num_count = defaultdict(int)
        self.freq_count = defaultdict(int)

    def add(self, number: int) -> None:
        old_freq = self.num_count[number]
        new_freq = old_freq + 1
        
        # Update number's frequency
        self.num_count[number] = new_freq
        
        # Update frequency tracking
        if old_freq > 0:
            self.freq_count[old_freq] -= 1
        self.freq_count[new_freq] += 1

    def deleteOne(self, number: int) -> None:
        old_freq = self.num_count[number]
        if old_freq == 0:
            return  # Number is not in the data structure
        
        new_freq = old_freq - 1
        
        # Update number's frequency
        self.num_count[number] = new_freq
        
        # Update frequency tracking
        self.freq_count[old_freq] -= 1
        if new_freq > 0:
            self.freq_count[new_freq] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_count[frequency] > 0