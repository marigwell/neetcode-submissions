class Solution:
    def isPalindrome(self, s: str) -> bool:
        # input: string s
        # output: bool - T / F
        # case sensitivty / alphanumeric chars
        # plan: two pointer

        left = 0
        right = len(s) - 1

        while left < right:
            # prevent pointers from crossing while skipping non-alphanumeric chars
            while left < right and not s[left].lower().isalnum():
                left += 1
            while left < right and not s[right].lower().isalnum():
                right -= 1
            
            # checks if left and right pointers match chars
            if s[left].lower() != s[right].lower():
                return False
            
            # move pointers
            left += 1
            right -= 1
                
        return True

