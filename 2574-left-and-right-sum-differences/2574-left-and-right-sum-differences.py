class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i+1:])
            ans.append(abs(left - right))
        return ans
        