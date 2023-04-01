class Solution {
    public long countSubarrays(int[] nums, int mink, int maxk) {
        boolean minf=false;
        boolean maxf=false;
        int mi=0,ma=0,s=0;
        long res=0;
        for(int i=0;i<nums.length;i++){
            int n=nums[i];
            if((n < mink )|| (n > maxk)){
                minf=false;
                maxf=false;
                s=i+1;
            }
            if(n==mink){
                minf=true;
                mi=i;
            }
            if(n==maxk){
                maxf=true;
                ma=i;
            }
            if(minf && maxf){
                res+=(Math.min(mi,ma)-s+1);
            }
        }
        return res;
    }
}