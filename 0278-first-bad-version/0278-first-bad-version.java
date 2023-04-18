/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        if(n==1){
            return n;
        }
        int l=1;
        int h=n;
        int m=(l+h)/2;
        while(l<=h){
            m=(l)+(h-l)/2;
            if(isBadVersion(m-1)==false && isBadVersion(m)==true){
                break;
            }
            
            else if(isBadVersion(m)==true){
                h=m-1;
            }
            else{
                l=m+1;
            }
            
        }
        return m;
    }
}