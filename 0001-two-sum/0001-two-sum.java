class Solution {
    public int[] twoSum(int[] nums, int t) {
        HashMap<Integer, Integer> map=new HashMap<>();
        int i,c;
        
        c=0;
        for(i=0;i<nums.length;i++){
            if(map.containsKey(nums[i])){
                c=map.get(nums[i]);
                break;
            }
            else map.put(t-nums[i],i);
        }
        int num[]={i,c};
        return num;
    }
}