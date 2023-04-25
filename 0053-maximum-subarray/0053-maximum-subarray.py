class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Finds the maximum sum of a contiguous subarray in the given list of
        integers using Kadane's algorithm.

        Args:
            nums (list[int]): A list of integers.

        Returns:
            int: The maximum sum of a contiguous subarray in the given list of
            integers.

        """
        if len(nums) == 1:
            return nums[0]
        else:
            current_sum = 0
            # Initialize to negative infinity to
            # handle cases with all negative numbers in the input array
            best_sum = float('-inf')

            for num in nums:
                current_sum = max(num, current_sum + num)
                best_sum = max(best_sum, current_sum)

            return best_sum