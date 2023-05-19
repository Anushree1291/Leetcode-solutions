class Solution {
    public int minOperations(String[] l) {
        int c=0;
        for(int i=0;i<l.length;i++){
            if(l[i].equals("../")){
                if(c>0) c--;
            }
            else if(l[i].equals("./")){
                continue;
            }
            else if(l[i].charAt(l[i].length()-1)=='/'){
                c++;
            }
        }
        return c;
    }
}