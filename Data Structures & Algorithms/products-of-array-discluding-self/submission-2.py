class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # attempt 2 - better space complexity
        # input: array of int
        # output: product of all elements except nums[i]
        # time: O(n)
        # space: O(1)
        results = []

        running = 1

        # stores left products directly to results
        for i in range(len(nums)):
            results.append(running)
            running *= nums[i]
        
        right_product = 1

        # fold right products directly into results
        for i in range(len(nums) - 1, -1, -1):
            results[i] *= right_product
            right_product*= nums[i]

        return results