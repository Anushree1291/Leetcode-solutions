class Solution {
    public int[][] floodFill(int[][] i, int sr, int sc, int nco) {
        if(i[sr][sc]!=nco){
            dfs(i,sr,sc,i[sr][sc],nco);
        }
        return i;
    }
    public void dfs(int[][] i, int r,int c,int co, int nco){
        if(i[r][c]==co){
            i[r][c]=nco;
            if(r>=1) dfs(i,r-1,c,co,nco);
            if(c>=1) dfs(i,r,c-1,co,nco);
            if(r<i.length-1) dfs(i,r+1,c,co,nco);
            if(c<i[0].length-1) dfs(i,r,c+1,co,nco);
        }
        
    }
    
}