class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        int i,j;
        List<Integer> a=new ArrayList<Integer>();
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        i=0;j=0;
        while(i<nums1.length && j<nums2.length){
            if(nums1[i]<nums2[j]){
                i++;
            }
            else if(nums1[i]>nums2[j]){
                j++;
            }
            else{
                a.add(nums1[i]);
                i++;j++;
            }
        }
        int[] arr = a.stream().mapToInt(k-> k).toArray();
        return arr;
    }
}