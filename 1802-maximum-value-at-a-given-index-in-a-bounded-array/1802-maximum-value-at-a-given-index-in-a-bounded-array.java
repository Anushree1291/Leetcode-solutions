class Solution {
    public int maxValue(int n, int in, int m) {
        int r=in;
        int l=in;
        int s=n;
        int h=1;
        while(s+r-l+1<=m){
            s+=r-l+1;
            r= r==n-1?n-1:r+1;
            l=l==0?0:l-1;
            h++;
            if(l==0 && r==n-1){
                int a=m-s;
                int st=(a/n);
                s+=st*n;
                h+=st;
            }
            
        }
        return h;
    }
}