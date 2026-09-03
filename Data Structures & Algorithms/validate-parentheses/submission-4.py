class Solution:
    def isValid(self, s: str) -> bool:
        # input: string s containing special characters
        # output: bool

        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in pairs.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()

        return len(stack) == 0