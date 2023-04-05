class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int x = 0;

        for (String operation : operations) {
            // since every element of the operations contains on 3 char
            // and the char at posiion 1 is either + or - , where
            // + is for increamenting and - is for decrementing 
            // i will use this as the comparism

            if (operation.charAt(1) == '+') {
                x++;
            } else {
                x--;
            }

        }
        return x;
    }
}