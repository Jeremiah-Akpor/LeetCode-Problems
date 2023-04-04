class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            c = target - nums[i]
            if (c in nums) and (nums.index(c) != i):
                j = nums.index(c)
                return [i,j]