from queue import PriorityQueue 
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        m={}
        for i in arr:
            if i not in m:
                m[i]=0
            m[i]+=1

        q = PriorityQueue()

        for i in m:
            q.put((m[i],i))
        
        for i in range(len(m)):
            p=q.get()
            if k>=p[0]:
                k-=p[0]
            else:
                return q.qsize()+1
        return 0