class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # input: array of int
        # output: product of all the elements of nums except the one at that index
        # time: O(n) - iterates through the whole array input
        # space: O(n) - creates helper arrays but grows same as input size
        left_products = []
        right_products = [1] * len(nums)

        results = [] 

        running = 1

        for i in range(len(nums)):
            left_products.append(running)
            running *= nums[i]
        
        running = 1

        for i in range(len(nums) - 1, -1, -1):
            right_products[i] = running
            running *= nums[i]

        for i in range(len(nums)):
            results.append(left_products[i] * right_products[i])

        return results