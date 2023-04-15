class Solution {
    Integer dp[][];
    
    public int maxValueOfCoins(List<List<Integer>> p, int k) {
        dp=new Integer[p.size()+1][k+1];
        return traversal(p,p.size()-1,k);
        
    }
    
    public int traversal(List<List<Integer>> p,int i,int k){
        if(i<0 || k==0){
            return 0;
        }
        if(dp[i][k]!=null) return dp[i][k];
        
        int n=Math.min(p.get(i).size(),k);
        
        int exclude = traversal(p,i-1,k);
        
        int include=0;
        for(int j=0,sum=0;j<n;j++){
            sum+=p.get(i).get(j);
            include=Math.max(sum+traversal(p,i-1,k-j-1),include);
        }
        dp[i][k]=Math.max(include,exclude);
        return dp[i][k];
    }
    
}