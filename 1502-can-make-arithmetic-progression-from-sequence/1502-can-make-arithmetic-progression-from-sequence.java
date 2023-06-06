class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        if(arr.length==2){
            return true;
        }
        Arrays.sort(arr);
        int c=arr[1]-arr[0];
        for(int i=0;i<arr.length-1;i++){
            if(c!=(arr[i+1]-arr[i])){
                return false;
            }
        }
        return true;
    }
}