class Solution {
    public int minInsertions(String s) {
        int a[][]=new int[s.length()+1][s.length()+1];
        for(int i=0;i<s.length()+1;i++){
            a[i][0]=0;
            a[0][i]=0;
            
        }
        StringBuffer sbr = new StringBuffer(s);
        String g=sbr.reverse().toString();
        for(int i=1;i<=s.length();i++){
            for(int j=1;j<=s.length();j++){
                if(s.charAt(i-1)==g.charAt(j-1)){
                    a[i][j]=a[i-1][j-1]+1;
                }
                else{
                    a[i][j]=Math.max(a[i-1][j],a[i][j-1]);
                }
            }
        }
        return s.length()-a[s.length()][s.length()];
    }
}