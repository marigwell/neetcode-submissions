class Solution:
    def isPalindrome(self, s: str) -> bool:
        # input: string s
        # output: bool - T / F
        # case sensitivty / alphanumeric chars
        # plan: two pointer

        left = 0
        right = len(s) - 1

        while left < right:
            while not s[left].lower().isalnum() and left < right:
                left += 1
            while not s[right].lower().isalnum() and left < right:
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
                
        return True

