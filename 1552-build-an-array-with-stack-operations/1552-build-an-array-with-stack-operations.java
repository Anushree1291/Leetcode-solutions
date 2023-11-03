class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> ar=new ArrayList<String>();
        int c=0;
        for(int i=1;i<=n;i++){
            if(c==target.length){
                break;
            }
            if(target[c]==i){
                ar.add("Push");
                c++;
            }
            else{
                ar.add("Push");
                ar.add("Pop");
            }
        }
        return ar;
    }
}