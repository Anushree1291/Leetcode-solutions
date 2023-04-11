class Solution {
    public int singleNumber(int[] n) {
        if(n.length==1){
            return n[0];
        }
        Arrays.sort(n);
        int c=0;
        if(n[0]!=n[1]){
            return n[0];
        }
        else if(n[n.length-1]!=n[n.length-2]){
            return n[n.length-1];
        }
        else{
            
            for(int i=1;i<n.length-2;i++){
                if(n[i-1]!=n[i] && n[i+1]!=n[i]){
                    c=n[i];
                }
            }
        }
        return c;
    }
}