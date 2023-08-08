class Solution {
    public int search(int[] nums, int t) {
        boolean b=false;
        int j=0;;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==t){
                j=i;
                b=true;
                break;
            }
        }
        if(!b){
            return -1;
        }
        else{
            return j;
        }
    }
}