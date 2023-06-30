from queue import PriorityQueue
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        q=PriorityQueue()
        n=len(nums1)
        m=len(nums2)
        q.put((nums1[0]+nums2[0],[0,0]))
        vis=set()
        l=[]
        vis.add((0,0))
        while k>0 and not q.empty():
            v,[i,j]=q.get()
            l.append([nums1[i],nums2[j]])
            
            if i+1<n and (i+1,j) not in vis:
                vis.add((i+1,j))
                q.put((nums1[i+1]+nums2[j],[i+1,j]))
            
            if j+1<m and (i,j+1) not in vis:
                vis.add((i,j+1))
                q.put((nums1[i]+nums2[j+1],[i,j+1]))
            k=k-1
            
        return l