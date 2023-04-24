class Solution {
    public boolean backspaceCompare(String s, String t) {
        return tra(s).equals(tra(t));
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