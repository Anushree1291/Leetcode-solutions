class Solution {
    public int minCostClimbingStairs(int[] c) {
        if(c.length==2){
            return c[0]>c[1]?c[1]:c[0];
        }
        int i=0;
        int j=2;
        while(j<c.length){
            i=Math.min(c[j-1],c[j-2]);
            c[j]+=i;
            j++;
        }
        i=c.length;
        return Math.min(c[i-1],c[i-2]);
    }
}