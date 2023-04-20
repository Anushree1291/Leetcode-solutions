class Solution {
    public String addStrings(String num1, String num2) {
        int c=0;
        StringBuilder s=new StringBuilder();
        int i=num1.length()-1;
        int j=num2.length()-1;
        while(i>=0 || j>=0){
            int a= i<0?0:num1.charAt(i)-'0';
            int b= j<0?0:num2.charAt(j)-'0';
            int sum=a+b+c;
            s.append(sum%10);
            c=sum/10;
            i--;
            j--;
        }
        if(c==1){
            s.append(c);
        }
        return s.reverse().toString();
    }
}