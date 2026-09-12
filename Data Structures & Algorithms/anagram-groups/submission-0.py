class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: array of strings
        # output: sublists of strings that are anagrams
        # anagram - a string that contains the same amount of characters as another string

        # map out num of character count to list of anagrams
        char_count = defaultdict(list)

        for s in strs:
            count = [0] * 26 # creates 26 slots (a - z)

            for char in s:
                # convert the character into an index from 0-25
                index = ord(char) - ord("a")

                # increment occurance by 1 of the character
                count[index] += 1
            
            # lists cannot be dictionary keys because they are mutable
            # convert the frequency list into an immutable tuple
            key = tuple(count)

            # add the original word to its anagram group
            char_count[key].append(s)

        # only need the grouped word lists
        return list(char_count.values())