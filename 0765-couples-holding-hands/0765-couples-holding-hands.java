class Solution {
    public int minSwapsCouples(int[] r) {
        Map<Integer,Integer> ar=new HashMap<Integer,Integer>();
        int s=0;
        for( int i=0; i<r.length;i++){
            ar.put(r[i],i);
        }
        for( int i=0; i<r.length;i+=2){
            int n=r[i]^1;
            if(r[i+1]!=n){
                s+=1;
                int p=ar.get(n);
                int t=r[i+1];
                r[i+1]=r[p];
                r[p]=t;
                ar.put(r[i+1],i+1);
                ar.put(r[p],p);
            }
        }
        return s;
    }
}