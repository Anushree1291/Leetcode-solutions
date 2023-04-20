class Solution {
    public int numIslands(char[][] g) {
        int c=0;
        for(int i=0;i<g.length;i++){
            for(int j=0;j<g[0].length;j++){
                if(g[i][j]=='1'){
                    c++;
                    tra(g,i,j);
                }
            }
        }
        return c;
    }
    public void tra(char[][] g, int i,int j){
        if(i<0 || j<0 || i>=g.length || j>=g[0].length || g[i][j]=='0'){
            return;
        }
        if(g[i][j]=='1'){
            g[i][j]='0';
            if(i>=1) tra(g,i-1,j);
            if(j>=1) tra(g,i,j-1);
            if(i<g.length-1) tra(g,i+1,j);
            if(j<g[0].length-1) tra(g,i,j+1);
        }
        return;
    }
}