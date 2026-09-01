class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # input: string s
        # output: int -> length of longest substring

        seen = set()
        left = 0
        right = 0
        max_length = 0

        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            current_length = right - left + 1
            if max_length < current_length:
                max_length = current_length
            right += 1
        return max_length