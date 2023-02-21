class Solution {
    public int singleNonDuplicate(int[] n) {
        int a=n[n.length-1];
        for(int i=0;i<n.length-1;i++){
            if(n[i]==n[i+1]){
                i++;
            }
            else{
                a=n[i];
                break;
            }
        }
        return a;
    }
}