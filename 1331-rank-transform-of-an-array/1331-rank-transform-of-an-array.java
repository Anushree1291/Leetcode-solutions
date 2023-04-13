class Solution {
    public int[] arrayRankTransform(int[] arr) {
        int a[]=Arrays.copyOf(arr,arr.length);
        Arrays.sort(a);
        Map<Integer,Integer> ar=new HashMap<Integer,Integer>();
        for(int i:a){
            ar.putIfAbsent(i,ar.size()+1);
        }
        for(int i=0;i<arr.length;i++){
            a[i]=ar.get(arr[i]);
        }
        return a;
    }
}