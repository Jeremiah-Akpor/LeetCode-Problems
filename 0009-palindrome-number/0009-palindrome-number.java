class Solution {
    public boolean isPalindrome(int x) {
        String str = x + "";
        StringBuilder sb = new StringBuilder(str);
        String rStr = sb.reverse().toString();
        return str.equals(rStr);

    }
}