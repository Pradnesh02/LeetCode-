class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_index = -1

class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """
        root = TrieNode()
        
        # Helper to decide if candidate index 'i' is strictly better than 'curr_best'
        def is_better(i, curr_best):
            if curr_best == -1:
                return True
            len_i = len(wordsContainer[i])
            len_best = len(wordsContainer[curr_best])
            if len_i != len_best:
                return len_i < len_best
            return i < curr_best

        # Insert reversed words into the Trie
        for i, word in enumerate(wordsContainer):
            curr = root
            if is_better(i, curr.best_index):
                curr.best_index = i
                
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                
                if is_better(i, curr.best_index):
                    curr.best_index = i

        # Process each query
        ans = []
        for q in wordsQuery:
            curr = root
            for char in reversed(q):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    break
            ans.append(curr.best_index)
            
        return ans