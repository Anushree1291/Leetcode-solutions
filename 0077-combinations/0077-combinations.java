class Solution {
    List<List<Integer>> arr=new LinkedList<List<Integer>>();
    
    public List<List<Integer>> combine(int n, int k) {
        List<Integer> ar=new LinkedList<Integer>();
        traversal(1,n,0,k,ar);
        return arr;
    }
    public void traversal(int s,int n,int r,int k,List<Integer> ar){
        if(r==k){
            arr.add(new LinkedList<>(ar));
            return;
        }
        for(int i=s;i<=n;i++){
            ar.add(i);
            traversal(i+1,n,r+1,k,ar);
            ar.remove(ar.size()-1);
        }
    }
}