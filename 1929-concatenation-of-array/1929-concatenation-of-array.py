class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # 1. get the length of the array
        length = len(nums)
        
        # 2. create an empty array of size 2n 
        ans = []
        
        """
        3. create for loop the iterates through the nums array
         and inserts the element of the nums array into the ans 
         array at position i and i+n
        """
        for i in range(0,length):
            ans.insert(i,nums[i] ) 
            ans.insert(i+length,nums[i] ) 
        
        return ans
        