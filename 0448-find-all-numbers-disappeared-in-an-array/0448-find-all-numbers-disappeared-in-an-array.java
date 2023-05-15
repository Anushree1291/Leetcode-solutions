class Solution {
    public List<Integer> findDisappearedNumbers(int[] n) {
        List<Integer> ar=new LinkedList<Integer>();
        for(int i=0;i<n.length;i++){
            if(n[Math.abs(n[i])-1]>0){
                n[Math.abs(n[i])-1]*=-1;
            }
        }
        for(int i=0;i<n.length;i++){
            if(n[i]>0){
                ar.add(i+1);
            }
        }
        return ar;
    }
}