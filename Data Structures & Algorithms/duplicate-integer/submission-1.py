class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # review - 1
        # input: array of int
        # output: bool - if any value appears more than once

        unique_values = set()

        for num in nums:
            if num in unique_values:
                return True

            unique_values.add(num)

        return False

