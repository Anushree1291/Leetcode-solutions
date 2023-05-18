class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> e) {
        List<Integer>[] aj=new LinkedList[n];
        for(int i=0;i<n;i++){
            aj[i]=new LinkedList<>();
        }
        boolean[] v=new boolean[n];
        for(List<Integer> i:e){
            aj[i.get(1)].add(i.get(0));
        }
        List<Integer> ar=new LinkedList<>();
        for(int i=0;i<n;i++){
            if(aj[i].size()==0){
                ar.add(i);
            }
        }
        return ar;
    }
}