class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        def backtrack(index, path):
            # Base case: if the current combination length matches digits length
            if index == len(digits):
                res.append("".join(path))
                return

            # Get letters corresponding to the current digit
            possible_letters = phone_map[digits[index]]

            # Explore all options for this digit
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()  # Backtrack

        backtrack(0, [])
        return res