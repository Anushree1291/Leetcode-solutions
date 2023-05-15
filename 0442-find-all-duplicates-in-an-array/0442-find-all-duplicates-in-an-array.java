class Solution {
    public List<Integer> findDuplicates(int[] n) {
        List<Integer> ar=new LinkedList<>();
        Set<Integer> a=new HashSet<>();
        for(int i=0;i<n.length;i++){
            if(a.contains(n[i])){
                ar.add(n[i]);
            }
            a.add(n[i]);
        }
        return ar;
    }
}