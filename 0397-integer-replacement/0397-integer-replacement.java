class Solution {
    Map<Integer,Integer> ar=new HashMap<>();
    public int integerReplacement(int n) {
        return tra(n);
    }
    public int tra(int n){
        if(ar.containsKey(n)){
            return ar.get(n);
        }
        if(n<0){
            return 31;
        }
        if(n<=1){
            return 0;
        }
        else if (n==2) return 1;

        int a=0;
        if(n%2==0){
            a=tra(n/2)+1;
        }
        else{
            a=Math.min(tra(n+1),tra(n-1))+1;
        }
        ar.put(n,a);
        return a;
    }
}