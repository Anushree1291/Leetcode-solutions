class Solution {
    public int removeDuplicates(int[] n) {
        int c=1;
        for(int i=1;i<n.length;i++){
            if(n[i-1]!=n[i]){
                n[c]=n[i];
                c++;
            }
        }
        return c;
    }
}