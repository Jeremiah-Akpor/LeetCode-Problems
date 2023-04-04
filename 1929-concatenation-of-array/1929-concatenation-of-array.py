class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # 1. get the length of the array
        length = len(nums)
        
        # 2. create an empty array of size 2n 
        ans = [0] * (2 * length)
        
        """
        3. use list comprehension to insert the element of the nums array 
           into the ans array at position i and i+n
        """
        ans[:length] = nums
        ans[length:] = nums
        
        return ans
        