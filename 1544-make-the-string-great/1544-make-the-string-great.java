class Solution {
    public String makeGood(String s) {
        String st="";
        Stack<Character> ar=new Stack<Character>();
        for(int i=0; i<=s.length()-1 ;i++){
            if(!ar.empty()){
                if(s.charAt(i)==ar.peek()+32 || s.charAt(i)==ar.peek()-32){
                    //System.out.println(s.charAt(i));
                    ar.pop();
                }
                else{
                    ar.push(s.charAt(i));
                }
            }
            else{
                ar.push(s.charAt(i));
            }
        }
        for(char ch : ar){
            st+=ch;
        }
        return st;
        
    }
}