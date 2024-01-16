class Solution {
    public List<List<Integer>> findWinners(int[][] m) {
        List<Integer> a1=new LinkedList<>();
        List<Integer> a2=new LinkedList<>();
        int a[]=new int[100001];
        Arrays.fill(a,-1);
        for(int i=0;i<m.length;i++){
            if(a[m[i][0]]==-1){
                a[m[i][0]]=0;
            }
            a[m[i][1]] = a[m[i][1]]==-1? 1:a[m[i][1]]+1;
        }
        for(int i=0;i<100001;i++){
            if(a[i]==-1){
                continue;
            }
            if(a[i]==0){
                a1.add(i);
            }
            else if(a[i]==1){
                a2.add(i);
            }
        }
        List<List<Integer>> arr=new LinkedList<>();
        arr.add(a1);
        arr.add(a2);
        return arr;
    }
}