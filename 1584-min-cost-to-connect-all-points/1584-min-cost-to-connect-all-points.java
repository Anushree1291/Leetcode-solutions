class Solution {
    public int minCostConnectPoints(int[][] p) {
        int a[]=new int[p.length];
        boolean b[]=new boolean[p.length];
        for (int i=0;i<p.length;i++){
            a[i]=Integer.MAX_VALUE;
        }
        b[0]=true;
        a[0]=0;
        int res=0;
        int c=0;
        int edge=0;
        while(edge++ < p.length-1){
            int min=Integer.MAX_VALUE;
            int next=-1;
            for(int i=0;i<p.length; ++i){
                if(!b[i]){
                    int dis=Math.abs(p[c][0]-p[i][0]) + Math.abs(p[c][1]-p[i][1]);
                    a[i]=Math.min(a[i],dis);
                    if(a[i] < min){
                        min = a[i];
                        next=i;
                    }
                }
            }
            System.out.println(c+" "+next);
            c=next;
            res+=min;
            b[c]=true;
        }
        return res;
    }
}