class Solution {
    public boolean backspaceCompare(String s, String t) {
        String a=tra(s);
        String b=tra(t);
        return a.equals(b);
    }
    public String tra(String s){
        int a=0;
        String st="";
        for(int i=s.length()-1;i>=0;i--){
            if(s.charAt(i)=='#'){
                a++;
            }
            else if(a>0){
                a--;
                continue;
            }
            else{
                st=s.charAt(i)+st;
            }
        }
        return st;
    }
}