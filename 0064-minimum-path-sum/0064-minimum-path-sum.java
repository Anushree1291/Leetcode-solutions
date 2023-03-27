class Solution {
    public int minPathSum(int[][] g) {
        
        int n=g.length;
        int m=g[0].length;
        int a[][]=new int[n][m];
        for(int i=0;i<n;i++){
            Arrays.fill(a[i],Integer.MAX_VALUE);
        }
        a[0][0]=g[0][0];
        //System.out.println(n+" "+m);
        PriorityQueue<List<Integer>> q= new PriorityQueue<>((x,y)-> x.get(0)-y.get(0));
        q.add(new ArrayList<>(Arrays.asList(g[0][0],0,0)));
        while(!q.isEmpty()){
            List<Integer> c=q.poll();
                    int d=c.get(1);
                    int e=c.get(2);
            if(c.get(1)==n-1 && c.get(2)==m-1){
                return c.get(0);
            }
                    if(d<n-1){
                        if(a[d+1][e]>c.get(0)+g[d+1][e]){
                            a[d+1][e]=c.get(0)+g[d+1][e];
                            q.add(new ArrayList<>(Arrays.asList(c.get(0)+g[d+1][e],d+1,e)));
                        }
                        //System.out.println((c.get(0)+g[d+1][e])+" "+(d+1)+" "+e);
                    }
                        
                    if(e<m-1){
                        if(a[d][e+1]>c.get(0)+g[d][e+1]){
                            a[d][e+1]=c.get(0)+g[d][e+1];
                            q.add(new ArrayList<>(Arrays.asList(c.get(0)+g[d][e+1],d,e+1)));
                        }
                        //System.out.println((c.get(0)+g[d][e+1])+" "+d+" "+(e+1));
                    }
        }
        List<Integer> c=q.poll();
        return c.get(0);
    }
}