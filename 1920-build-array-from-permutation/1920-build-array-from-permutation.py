class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        # 1. get the length of the array
        n = len(nums)

        """
            The code creates a new list ans with the same length as the input list nums,
            where each element in the new list is initialized to zero.
            For example, if nums is [2, 5, 3, 7], the code ans = [0] * len(nums) will 
            create a new list ans with the elements [0, 0, 0, 0].
        """
        ans = [0] * n

        # 3. create for loop then iterates through the nums array
        # and inserts the element of the nums array into the ans 
        # array 
        for i in range(n):
            ans[i] = nums[nums[i]]
        
        return ans
        