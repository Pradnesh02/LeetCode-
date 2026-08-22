class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end = False


class Solution(object):
    def replaceWords(self, dictionary, sentence):
        root = TrieNode()
        
        # Build the Trie from dictionary
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True
            
        def find_shortest_root(word):
            node = root
            prefix = []
            for char in word:
                if char not in node.children:
                    return word
                node = node.children[char]
                prefix.append(char)
                if node.is_end:
                    return "".join(prefix)
            return word

        # Replace each word in the sentence
        words = sentence.split()
        return " ".join(find_shortest_root(w) for w in words)