class Solution {
    
    /**
     * @param nums: int[]
     * @return int[]
     */
    public int[] getConcatenation(int[] nums) {
        // 1. get the length of the array
        int length = nums.length;

        // 2. create an empty array of size 2n 
        int[] ans = new int[length * 2];

        // 3. create for loop the iterates through the nums array
        // and inserts the element of the nums array into the ans 
        // array at position i and i+n
        for (int i = 0; i < nums.length; i++) {
            ans[i] = nums[i];
            ans[i + length ] = nums[i];
        }
        
        return ans;
    }
}
