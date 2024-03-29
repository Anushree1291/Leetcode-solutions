class Solution {
    public int minScore(int n, int[][] r) {
        List<Integer>[] ar=new LinkedList[n];
        List<Integer>[] c=new LinkedList[n];
        boolean[] v=new boolean[n];
        for(int i=0;i<n;i++){
            ar[i]=new LinkedList<>();
            c[i]=new LinkedList<>();
        }
        for(int i=0;i<r.length;i++){
            int w=r[i][0]-1;
            int u=r[i][1]-1;
            ar[w].add(u);
            c[w].add(r[i][2]);
            ar[u].add(w);
            c[u].add(r[i][2]);
        }
        v[0]=true;
        int m=Integer.MAX_VALUE;
        Queue<Integer> q=new LinkedList<>();
        q.offer(0);
        while(!q.isEmpty()){
            int a=q.poll();
            for(int u:ar[a]){
                if(!v[u]){
                    v[u]=true;
                    q.offer(u);
                }
            }
            for(int u:c[a]){
                m=Math.min(u,m);
            }
        }
        return v[n-1]==true?m:-1;
    }
}