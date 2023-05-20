class Solution {
    public int[] productExceptSelf(int[] n) {
        int res[]=new int[n.length];
        int a=1;
        res[0]=1;
        for(int i=1;i<n.length;i++){
            res[i]=res[i-1]*n[i-1];
        }
        for(int i=n.length-1;i>=0;i--){
            res[i]=res[i]*a;
            a=a*n[i];
        }
        return res;
    }
}