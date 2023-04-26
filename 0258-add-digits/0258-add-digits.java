class Solution {
    public int addDigits(int num) {
        int s=0;
        while(num>9){
            while(num!=0){
                s+=num%10;
                num/=10;
            }
            num=s;
            s=0;
        }
        return num;
    }
}