class Solution {
    public int uniquePaths(int m, int n) {
        int a[][]=new int[m+1][n+1];
        for(int i=0;i<=m;i++){
            a[i][0]=0;
        }
        for(int i=0;i<=n;i++){
            a[0][i]=0;
        }
        a[1][1]=1;
        for(int i=1;i<=m;i++){
            for(int j=1;j<=n;j++){
                a[i][j]+=a[i-1][j]+a[i][j-1];
            }
        }
        //System.out.println(Arrays.deepToString(a));
        return a[m][n];
    }
}