class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # input: list of int 
        # output: list(s) of triplets that equal zero - must not contain any duplicate triplets and any order


        results = []
        nums.sort() # sorts from least to greatest

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right] 

                if current_sum < 0:
                    left += 1
                
                if current_sum > 0:
                    right -= 1

                if current_sum == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
            
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return results 