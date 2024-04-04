class Solution {
    public int maxDepth(String s) {
        int i,m,c;
        m=0;c=0;
        for(char ch:s.toCharArray()){
            c= ch=='(' ? ++c:c;
            c= ch==')' ? --c:c;
            m= c>m ? c:m;
        }
        return m;
    }
}