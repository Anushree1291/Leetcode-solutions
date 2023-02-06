class Solution {
    public int maxRotateFunction(int[] n) {
        int ar[]=new int[n.length];
        int a=0;
        int s=0;
        int b=0;
        for(int j:n){
            s+=j;
            b+=a*j;
            a++;
        }
        ar[0]=b;
        b=ar[0];
        for(int i=1;i<n.length;i++){
            ar[i]=ar[i-1]+s-a*n[a-i];
            b=Math.max(b,ar[i]);
        }
        return b;
    }
}