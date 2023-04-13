class Solution {
    public boolean validateStackSequences(int[] p, int[] po) {
        Stack<Integer> ar =new Stack<>();
        int j=0;
        
        for(int i=0;i<p.length;i++){
            ar.push(p[i]);
            while(!ar.isEmpty() &&  j<p.length && ar.peek()==po[j]){
                j++;
                ar.pop();
            }
        }
        if( j==po.length)
            return true;
        return false;
    }
}