"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for x in s:
            if x == '(':stack+=[1]
            elif x == '[':stack+=[2]
            elif x == '{':stack+=[3]
            else:
                if stack == []:return False
                elif (x == ')' and stack[-1] == 1) or (x == ']' and stack[-1] == 2) or (x == '}' and stack[-1] == 3):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        
        
"""
implement in stack, one thing need notice, the sequence of line 19 and 20, should determine if stack is empty, otherwise the stack[-1] will trigger error.
"""
