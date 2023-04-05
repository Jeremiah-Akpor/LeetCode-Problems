class Solution {
    public int[] shuffle(int[] nums, int n) {
        
        // create an empty array
        int[] ans = new int[n * 2];
        
        int i = 0;
        int j = 1;
        while  (  i < n) {
            ans[i+i] = nums[i];
            ans[j] = nums[i + n];
            j = j + 2;
            i++;
        }
        return ans;
    }
}