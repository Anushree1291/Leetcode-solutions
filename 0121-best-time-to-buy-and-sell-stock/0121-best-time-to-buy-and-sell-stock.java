class Solution {
    public int maxProfit(int[] p) {
        int m,pr,i;
        m=0;
        pr=0;
        for(i=0;i<p.length;i++){
            if(p[i]<p[m]){
                m=i;
            }
            else if(p[i]-p[m] >pr){
                pr=p[i]-p[m];
            }
        }
        return pr;
    }
}