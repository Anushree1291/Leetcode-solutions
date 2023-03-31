class Solution:
    def intersect(self, n1: List[int], n2: List[int]) -> List[int]:
        a=[]
        nums1=sorted(n1)
        nums2=sorted(n2)
        i=0
        j=0
        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i]>nums2[j]):
                j=j+1
            elif(nums1[i]<nums2[j]):
                i=i+1
            else:
                a.append(nums1[i])
                i=i+1
                j=j+1
        return a