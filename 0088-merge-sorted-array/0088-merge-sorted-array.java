import java.util.Arrays.*;
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i,j;
        j=0;
        for(i=m;i<m+n;i++){
            nums1[i]=nums2[j];
            j++;
        }
        for(i = m; i < nums1.length; i++) {
			int temp = nums1[i];
			int k = i - 1;
			
			while(k >= 0 && nums1[k] > temp) {
				nums1[k+1] = nums1[k];
				k--;
			}
			nums1[k+1] = temp;
		}
        //Arrays.sort(nums1);
    }
}