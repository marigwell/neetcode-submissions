class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping_par = {')' : '(', '}' : '{', ']' : '[' }

        for char in s:
            if char in mapping_par:
                if stack and stack[-1] == mapping_par[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False
        