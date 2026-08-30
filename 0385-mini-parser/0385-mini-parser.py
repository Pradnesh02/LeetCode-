# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if not s:
            return NestedInteger()

        # Case 1: If string is just a single integer (not wrapped in brackets)
        if s[0] != "[":
            return NestedInteger(int(s))

        stack = []
        num = None
        sign = 1

        for char in s:
            if char == "[":
                # Start of a new list
                stack.append(NestedInteger())
            elif char == "-":
                sign = -1
            elif char.isdigit():
                if num is None:
                    num = 0
                num = num * 10 + int(char)
            elif char in (",", "]"):
                # Append completed integer if one was being parsed
                if num is not None:
                    stack[-1].add(NestedInteger(sign * num))
                    num = None
                    sign = 1

                # End of a list
                if char == "]" and len(stack) > 1:
                    completed_list = stack.pop()
                    stack[-1].add(completed_list)

        return stack[0]