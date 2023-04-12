class Solution {
    public String simplifyPath(String path) {
        Stack<String> ar=new Stack<>();
        
        for(String s: path.split("/")){
            if(s.equals("..") && !ar.isEmpty()){
                ar.pop();
            }
            else if(!s.equals(".") && !s.equals("") && !s.equals("..")){
                ar.push(s);
            }
        }
        return ("/"+String.join("/",ar));
    }
}