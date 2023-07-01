from queue import PriorityQueue
class Solution:
    def kthSmallest(self, m: List[List[int]], k: int) -> int:
        v=0
        n=len(m)
        li=PriorityQueue()
        li.put((m[0][0],(0,0)))
        vis=set()
        vis.add((0,0))
        while k!=0 and not li.empty():
            v,(i,j)=li.get()
            k-=1
            if i+1<n and (i+1,j) not in vis:
                vis.add((i+1,j))
                li.put((m[i+1][j],(i+1,j)))
            
            if j+1<n and (i,j+1) not in vis:
                vis.add((i,j+1))
                li.put((m[i][j+1],(i,j+1)))
        return v