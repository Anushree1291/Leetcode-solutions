class Solution {
    public int[][] generateMatrix(int n) {
        int a[][]=new int[n][n];
        int r=0;
        int re=n-1;
        int c=0;
        int ce=n-1;
        int j=1;
        while(r<=re && c<=ce){
            for(int i=c;i<=ce;i++){
                a[r][i]=j;
                j++;
            }
            r++;
            for(int i=r;i<=re;i++){
                a[i][ce]=j;
                j++;
            }
            ce--;
            if(c<=ce){
                for(int i=ce;i>=c;i--){
                    a[re][i]=j;
                    j++;
                }
            }
            re--;
            if(r<=re){
                for(int i=re;i>=r;i--){
                    a[i][c]=j;
                    j++;
                }
            }
            c++;
            
        }
        return a;
    }
}