class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x = 0
        ans = []
        for num in nums:
            x = x + num
            ans.append(x)
        return ans