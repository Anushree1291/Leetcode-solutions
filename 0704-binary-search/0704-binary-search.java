class Solution {
    public int search(int[] nums, int target) {
        List<Integer> ar =Arrays.stream(nums).boxed().collect(Collectors.toList()); 
        return ar.indexOf(target);
    }
}