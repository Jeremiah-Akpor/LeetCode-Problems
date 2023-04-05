class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        
        """
        The first for loop Returns:
            A list of integers where the i-th element is the sum of the first i+1
            elements in the input list.

        Example:
            >>> compute_running_sum([1, 2, 3, 4])
            [1, 3, 6, 10]
        
        The second for loop calculates the absolute difference between the sum of the first i-1 elements
        and the sum of the last n-i+1 elements, for i in the range 1 to n-1 inclusive.
        """
        x = 0
        temp = []
        for num in nums:
            x += num
            temp.append(x)
        
        ans = []
        last = temp[-1]
        ans.append(last - nums[0])
        for i in range(1, len(nums)):
            right = last - temp[i]
            left = temp[i-1]
            ans.append(abs(left - right))
        return ans