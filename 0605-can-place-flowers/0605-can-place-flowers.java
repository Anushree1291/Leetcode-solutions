class Solution {
    public boolean canPlaceFlowers(int[] f, int n) {
        if(n==0) return true;
        if(f.length==1){
            if(f[0]==0) return true;
            else return false;
        }
        for(int i=0;i<f.length;i++){
            int t=0;
            if(i==0){
                t=f[i+1]+f[i];
            }
            else if(i==f.length-1){
                t=f[i]+f[i-1];
            }
            else{
                t=f[i-1]+f[i]+f[i+1];
            }
            if(t==0){
                n--;
                f[i]=1;
            }
        }
        if(n<=0){
            return true;
        }
        return false;
    }
}