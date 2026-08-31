class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if both str are not same len
        if len(s) != len(t):
            return False

        counts = {}

        for char in s:
            counts[char] = counts.get(char, 0) + 1
            
        for char in t:
            if char in counts:
                counts[char] = counts[char] - 1
                
                if counts[char] < 0:
                    return False
            else:
                return False

        return True
            