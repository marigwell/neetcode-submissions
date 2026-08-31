class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make a dictionary to keep in track of the indices and the associated number of the index
        # iterate through the list of nums based on length to keep in track of current index
        # get the difference of target and current index's number
        # if the difference is in the dictionary, return the pair indices of the difference and current number index
        # otherwise, place the index and associated number inside the dictionary

        nums_dict = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if (diff in nums_dict):
                return [nums_dict[diff], i]
            nums_dict[nums[i]] = i

        return []

        