class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a=n-1;
        b=m-1;
        i=m+n-1
        while a>=0:
            if (b>=0 and nums1[b]>nums2[a]):
                nums1[i]=nums1[b];
                i=i-1
                b=b-1
            else:
                nums1[i]=nums2[a]
                i=i-1
                a=a-1
        return nums1