class Solution:
    def isValid(self, string: str) -> bool:
        p_dict = {")": '(', "]": '[', "}": '{'}
        stack = []  # Create an empty stack
        open_p = {"(", "[", "{"}
        for parentheses in string:
            if parentheses in p_dict and p_dict[parentheses] not in stack:
                return False
            if parentheses in open_p:
                stack.append(parentheses)
            elif len(stack) != 0 and stack[-1] == p_dict[parentheses]:
                stack.pop()  # Pop the top item from the stack
        return len(stack) == 0
