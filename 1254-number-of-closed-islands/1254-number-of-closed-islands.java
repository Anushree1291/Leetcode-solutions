class Solution {
    public int closedIsland(int[][] g) {
        
        boolean b[][]=new boolean[g.length][g[0].length];
        int c=0;
        for(int i=0;i<g.length;i++){
            for(int j=0;j<g[0].length;j++){
                if(g[i][j]==0  &&  !b[i][j] &&  dfs(i,j,g,b)){
                    c++;
                }
            }
        }
        return c;
    }
    
    public boolean dfs(int i,int j, int[][] g, boolean[][] b){
        if(i<0 || j<0 || i>=g.length || j>=g[0].length){
            return false;
        }
        if(b[i][j] || g[i][j]==1) return true;
        
        b[i][j]=true;
        boolean d=true;
        int[] d1={0,1,0,-1};
        int[] d2={-1,0,1,0};
        for(int x=0;x<4;x++){
            int r=i+d1[x];
            int c=j+d2[x];
            if(!dfs(r,c,g,b)){
                d=false;
            }
        }
        return d;
    } 
    
}