class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        vowels = set('aeiou')
        
        def devowel(word):
            return "".join('*' if ch in vowels else ch for ch in word.lower())
        
        words_perfect = set(wordlist)
        words_cap = {}
        words_vow = {}
        
        # Preprocess wordlist (preserving first occurrence precedence)
        for word in wordlist:
            lower = word.lower()
            if lower not in words_cap:
                words_cap[lower] = word
                
            masked = devowel(word)
            if masked not in words_vow:
                words_vow[masked] = word
                
        def solve_query(query):
            # 1. Exact match
            if query in words_perfect:
                return query
            
            # 2. Case-insensitive match
            lower = query.lower()
            if lower in words_cap:
                return words_cap[lower]
            
            # 3. Vowel error match
            masked = devowel(query)
            if masked in words_vow:
                return words_vow[masked]
            
            # 4. No match
            return ""
            
        return [solve_query(q) for q in queries]