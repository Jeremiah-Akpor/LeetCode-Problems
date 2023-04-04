class Solution {
    public int[] buildArray(int[] nums) {
        // 1. get the length of the array
        int length = nums.length;

        // 2. create an empty array of size 2n 
        int[] ans = new int[length];

        // 3. create for loop then iterates through the nums array
        // and inserts the element of the nums array into the ans 
        // array 
        for (int i = 0; i < length; i++) {
            ans[i] = nums[nums[i]];
        }
        
        return ans;
    }
}