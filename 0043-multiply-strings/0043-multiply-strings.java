class Solution {
    public String multiply(String n1, String n2) {
        int a[]=new int[n1.length()+n2.length()];
        for(int i=n1.length()-1;i>=0;i--){
            for(int j=n2.length()-1;j>=0;j--){
                a[i+j+1]+=(n1.charAt(i)-'0')*(n2.charAt(j)-'0');
                a[i+j]+=a[i+j+1]/10;
                a[i+j+1]=a[i+j+1]%10;
            }
        }
        int i=0;
        while(i<a.length && a[i]==0) i++;
        String s="";
        for(;i<a.length;i++){
            s+=a[i];
        }
        if(s.length()>=1)
        return s;
        else return "0";
    }
}