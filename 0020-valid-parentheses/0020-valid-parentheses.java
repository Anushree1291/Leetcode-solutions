class Solution {
    public boolean isValid(String s) {
        Stack<Character> ar = new Stack<Character>();
        for(char ch:s.toCharArray()){
            if(ch=='('){
                ar.push(ch);
            }
            else if(ch=='{'){
                ar.push(ch);
            }
            else if(ch=='['){
                ar.push(ch);
            }
            else if(ch==')'){
                if(!ar.empty() && ar.peek()=='(')
                    ar.pop();
                else{
                    ar.push(ch);
                }
            }
            else if(ch=='}'){
                if(!ar.empty() && ar.peek()=='{')
                    ar.pop();
                else{
                    ar.push(ch);
                }
            }
            else if(ch==']'){
                if(!ar.empty() && ar.peek()=='[')
                    ar.pop();
                else{
                    ar.push(ch);
                }
            }
            else{
                ar.push(ch);
            }
        }
        if(ar.size()==0){
            return true;
        }
        else 
            return false;
    }
}