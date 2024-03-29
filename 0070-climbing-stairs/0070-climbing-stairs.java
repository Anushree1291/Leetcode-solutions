class Solution {
    public int climbStairs(int n) {
        if(n==0){
            return 0;
        }
        else if(n==1){
            return 1;
        }
        int a[]=new int[n+1];
        Arrays.fill(a,-1);
        a[0]=0;
        a[1]=1;
        a[2]=2;
        int x=traversal(n,a);
        return x;
    }
    public int traversal(int n,int[] a){
        if(a[n]==-1){
            a[n]=traversal(n-1,a)+traversal(n-2,a);
        }
        return a[n];
    }
}