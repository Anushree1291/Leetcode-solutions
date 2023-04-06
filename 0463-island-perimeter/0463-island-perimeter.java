class Solution {
    public int islandPerimeter(int[][] g) {
        
        boolean b[][]=new boolean[g.length][g[0].length];
        for(int i=0;i<g.length;i++){
            for (int j=0;j<g[0].length;j++){
                if(g[i][j]==1 && !b[i][j]){
                    return dfs(i,j,g,b);
                }
            }
        }
        return 0;
    }
    public int dfs(int i,int j,int[][] g,boolean[][] b){
        if(i<0 || j<0 || i>=g.length || j>=g[0].length){
            return 1;
        }
        if(g[i][j]==0) return 1;
        if(b[i][j]) return 0;
        
        b[i][j]=true;
        int ans=0;
        int[] d1={0,1,0,-1};
        int[] d2={1,0,-1,0};
        for(int x=0;x<4;x++){
            int r=i+d1[x];
            int c=j+d2[x];
            ans+=dfs(r,c,g,b);
        }
        return ans;
    }
}