class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # input: array of int - sorted in non-decreasing order (least to greatest)
        # output: indices of two numbers that add up the target 
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
            # 1-indexed - indices start at 1
                return [left + 1, right + 1]