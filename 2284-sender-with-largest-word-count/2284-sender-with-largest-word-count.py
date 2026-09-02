from collections import defaultdict

class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        word_counts = defaultdict(int)
        
        for msg, sender in zip(messages, senders):
            word_counts[sender] += msg.count(' ') + 1
            
        best_sender = ""
        max_words = -1
        
        for sender, count in word_counts.items():
            if (count, sender) > (max_words, best_sender):
                max_words = count
                best_sender = sender
                
        return best_sender