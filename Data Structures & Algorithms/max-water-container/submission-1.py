class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # input: list of int - contains heights of water
        # output: int - maximum of water a container can store
        # time: O(n)
        # space: O(1)

        max_water = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            max_water = max(max_water, area)

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_water