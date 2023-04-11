class Solution {
    public String removeStars(String st) {
        Stack<Character> ar=new Stack<>();
        for(int i=0;i<st.length();i++){
            char ch=st.charAt(i);
            if(ch=='*'){
                ar.pop();
            }
            else{
                ar.push(ch);
            }
        }
        String s="";
        for(char ch:ar){
            s+=ch;
        }
        return s;
    }
}