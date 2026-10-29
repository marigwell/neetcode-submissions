class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # attempt 2
        # input: two strings
        # output: bool - true if both strings contain the same characters regardless of order
        if len(s) != len(t):
            return False

        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1

        for char in t:
            if char in counts:
                counts[char] = counts.get(char) - 1
            
                if counts[char] < 0:
                    return False
            else:
                return False

        return True
            