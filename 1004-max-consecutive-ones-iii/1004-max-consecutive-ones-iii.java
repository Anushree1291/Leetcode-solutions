class Solution {
    public int longestOnes(int[] n, int k) {
        int i,j;
        i=0;
        j=0;
        while(i<n.length){
            if(n[i]==0){
                k--;
            }
            if(k<0){
                if(n[j]==0){
                    k++;
                }
                j++;
            }
            i++;
        }
        return i-j;
    }
}