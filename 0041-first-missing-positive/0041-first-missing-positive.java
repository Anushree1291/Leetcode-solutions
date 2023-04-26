class Solution {
    public int firstMissingPositive(int[] n) {
        for(int i=0;i<n.length;i++){
            while(n[i]>0 && n[i] <= n.length && n[n[i]-1]!=n[i]){
                int t=n[i];
                n[i]=n[n[i]-1];
                n[t-1]=t;
            }
        }
        for(int i=0;i<n.length;i++){
            if(i+1!=n[i]){
                return i+1;
            }
        }
        return n.length+1;
    }
}