class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use a set for uniqueness
        # iterate the array into the set
        # if the character is in the set
        # return True
        # otherwise keep going then return false

        set_x = set()

        for num in nums:

            if num in set_x:
                return True
                
            set_x.add(num)
        
        return False