class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # A valid parentheses string must have an even length
        if len(s) % 2 != 0:
            return False

        # Forward pass: verify we don't have too many locked ')'
        open_slots = 0
        for char, lock in zip(s, locked):
            if lock == '0' or char == '(':
                open_slots += 1
            else:
                open_slots -= 1

            if open_slots < 0:
                return False

        # Backward pass: verify we don't have too many locked '('
        close_slots = 0
        for char, lock in zip(reversed(s), reversed(locked)):
            if lock == '0' or char == ')':
                close_slots += 1
            else:
                close_slots -= 1

            if close_slots < 0:
                return False

        return True