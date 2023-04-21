class Solution {
    int a[][][];
    int mod = 1000000007;
    
    public int profitableSchemes(int n, int m, int[] g, int[] p) {
        a=new int[101][101][101];
        for(int i=0;i<=g.length;i++){
            for(int j=0;j<=n;j++){
                Arrays.fill(a[i][j],-1);
            }
        }
        return tra(0,0,0,n,m,g,p);
    }
    public int tra(int in, int c, int p, int n, int m, int[] g, int[] pr){
        if(in==g.length){
            return p>=m?1:0;
        }
        if(a[in][c][p]!=-1){
            return a[in][c][p];
        }
        
        long t=(long)tra(in+1,c,p,n,m,g,pr);
        
        if(c+g[in]<=n)
            t+=tra(in+1,c+g[in],Math.min(m,p+pr[in]),n,m,g,pr);
        
        return a[in][c][p]=(int)(t%mod);
        
    }
}