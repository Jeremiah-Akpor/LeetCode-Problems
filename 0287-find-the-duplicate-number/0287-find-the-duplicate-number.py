class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numsDict = {}
        for num in nums:
            if num in numsDict:
                return num
            else:
        
                numsDict[num] = 1
            
