class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
       
        # 1. create an empty array 
        ans = [] 

        # 3. create for loop then iterates through the nums array
        # and append the element of the nums array into the ans 
        # array 
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        
        return ans
        