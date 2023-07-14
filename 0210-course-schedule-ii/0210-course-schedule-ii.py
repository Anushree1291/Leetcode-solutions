class Solution:
    def findOrder(self, n: int, p: List[List[int]]) -> List[int]:
        adj=[[] for _ in range(n)]
        ind=[0]*n
        for i in p:
            adj[i[1]].append(i[0])
            ind[i[0]]+=1
        
        q=deque()
        c=0
        for i in range(n):
            if ind[i]==0:
                q.append(i)
        
        l=[]
        
        while q:
            nd=q.popleft()
            l.append(nd)
            c+=1
            
            for i in adj[nd]:
                ind[i]-=1
                if ind[i]==0:
                    q.append(i)
        
        if c==n:
            return l
        return []
        