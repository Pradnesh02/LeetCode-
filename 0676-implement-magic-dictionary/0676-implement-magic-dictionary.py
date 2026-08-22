from collections import defaultdict

class MagicDictionary(object):

    def __init__(self):
        self.words_by_len = defaultdict(list)

    def buildDict(self, dictionary):
        for word in dictionary:
            self.words_by_len[len(word)].append(word)

    def search(self, searchWord):
        n = len(searchWord)
        if n not in self.words_by_len:
            return False
            
        for word in self.words_by_len[n]:
            # Count the number of differing characters
            diff_count = 0
            for c1, c2 in zip(searchWord, word):
                if c1 != c2:
                    diff_count += 1
                    if diff_count > 1:
                        break
            
            if diff_count == 1:
                return True
                
        return False