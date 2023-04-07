class Solution {
    public int maxAreaOfIsland(int[][] g) {
        
        boolean b[][] =new boolean[g.length][g[0].length];
        int m=0;
        for(int i=0;i<g.length;i++){
            for(int j=0;j<g[0].length;j++){
                if(g[i][j]==1 && !b[i][j]){
                     m=Math.max(m,dfs(i,j,g,b));
                }
            }
        }
        return m;
    }
    public int dfs(int i, int j, int[][] g, boolean[][] b){
        int c=0;
        if(g[i][j]==1 && !b[i][j]){
            b[i][j]=true;c=1;
            if(i>=1){
                c+=dfs(i-1,j,g,b);
            }
            if(j>=1){
                c+=dfs(i,j-1,g,b);
            }
            if(i<g.length-1){
                c+=dfs(i+1,j,g,b);
            }
            if(j<g[0].length-1){
                c+=dfs(i,j+1,g,b);
            }
        }
        return c;
    }
}