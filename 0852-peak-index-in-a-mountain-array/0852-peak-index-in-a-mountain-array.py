class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        h=len(arr)
        l=0
        
        while h>l:
            m=(l+h)//2
            if arr[m]<arr[m+1]:
                l=m+1
            else:
                h=m
        return l