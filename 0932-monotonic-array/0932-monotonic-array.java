class Solution {
    public boolean isMonotonic(int[] n) {
        if(n.length==1){
            return true;
        }
        boolean b=true;
        boolean c=true;
        for(int i=0;i<n.length-1;i++){
            if(!(n[i]<=n[i+1])){
                b=false;
                break;
            }
        }
        for(int i=n.length-1;i>0;i--){
            if(!(n[i]<=n[i-1])){
                c=false;
                break;
            }
        }
        if(!b && !c){
            return false;
        }
        else{
            return true;
        }
    }
}