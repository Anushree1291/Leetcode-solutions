class Solution {
    public int getMinDistance(int[] n, int t, int s) {
        int m=Integer.MAX_VALUE;
        for(int i=0;i<n.length;i++){
            if(n[i]==t){
                m=Math.min(m,Math.abs(s-i));
            }
        }
        return m;
    }
}