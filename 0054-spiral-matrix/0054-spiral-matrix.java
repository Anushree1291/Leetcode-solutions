class Solution {
    public List<Integer> spiralOrder(int[][] m) {
        List<Integer> ar=new LinkedList<>();
        if(m.length==0){
            return ar;
        }
        int r0=0;
        int c0=0;
        int r1=m.length-1;
        int c1=m[0].length-1;
        while(r0<=r1 && c0<=c1){
            for(int i=c0;i<=c1;i++){
                ar.add(m[r0][i]);
            }
            r0++;
            for(int i=r0;i<=r1;i++){
                ar.add(m[i][c1]);
            }
            c1--;
            if(r0<=r1){
                for(int i=c1;i>=c0;i--){
                    ar.add(m[r1][i]);
                }
            }
            r1--;
            if(c0<=c1){
                for(int i=r1;i>=r0;i--){
                    ar.add(m[i][c0]);
                }
            }
            c0++;
        }
        return ar;
    }
}