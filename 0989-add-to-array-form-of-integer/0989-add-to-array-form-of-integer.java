class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        int n=num.length;
        List<Integer> ar=new ArrayList();
        int i=n;
        while(--i>=0 || k>0){
            if(i>=0){
                k+=num[i];
            }
            ar.add(k%10);
            k/=10;
        }
        Collections.reverse(ar);
        return ar;
    }
}