class Solution {
    public int findPoisonedDuration(int[] t, int d) {
        if(t.length==0){
            return 0;
        }
        int re=0;
        for(int i=0;i<t.length-1;i++){
            re+=Math.min(t[i+1]-t[i],d);
        }
        return re+d;
    }
}