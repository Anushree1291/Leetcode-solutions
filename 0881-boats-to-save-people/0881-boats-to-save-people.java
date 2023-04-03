class Solution {
    public int numRescueBoats(int[] p, int l) {
        int ans=0;
        Arrays.sort(p);
        int j=0;
        for(int i=p.length-1;i>=0;i--){
            if(j>i){
                break;
            }
            ans++;
            if(p[j]+p[i]<=l){
                j++;
            }
        }
        return ans;
    }
}