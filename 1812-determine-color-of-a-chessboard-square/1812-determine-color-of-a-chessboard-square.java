class Solution {
    public boolean squareIsWhite(String c) {
        int a=c.charAt(0)-'a'+1;
        int b=c.charAt(1)-'0';
        if((a%2==0 && b%2==0) || (a%2==1 && b%2==1)){
            return false;
        }
        return true;
    }
}