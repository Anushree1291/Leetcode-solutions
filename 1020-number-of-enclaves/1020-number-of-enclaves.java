class Solution {
    public int numEnclaves(int[][] g) {
        for(int i=0;i<g.length;i++){
            if(g[i][0]==1){
                dfs(i,0,g);
            }
            if(g[i][g[0].length-1]==1){
                dfs(i,g[0].length-1,g);
            }
        }
        for(int i=1;i<g[0].length-1;i++){
            if(g[0][i]==1){
                dfs(0,i,g);
            }
            if(g[g.length-1][i]==1){
                dfs(g.length-1,i,g);
            }
        }
        int c=0;
        for(int i=1;i<g.length-1;i++){
            for(int j=1;j<g[0].length-1;j++){
                c+=g[i][j];
            }
        }
        return c;
    }
    public void dfs(int i,int j,int[][] g){
        if(i==-1 || j==-1 || i==g.length || j==g[0].length || g[i][j]==0){
            return;
        }
        g[i][j]=0;
        dfs(i+1,j,g);
        dfs(i,j+1,g);
        dfs(i-1,j,g);
        dfs(i,j-1,g);
    }
}