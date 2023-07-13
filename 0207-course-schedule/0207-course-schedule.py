class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        ind=[0]*n
        adj=[[] for _ in range(n)]
        
        for i in p:
            adj[i[1]].append(i[0])
            ind[i[0]]+=1
        
        q=deque()
        for i in range(n):
            if ind[i]==0:
                q.append(i)
        
        nvis=0
        
        while q:
            nd=q.popleft()
            nvis+=1
            
            for i in adj[nd]:
                ind[i]-=1
                if(ind[i]==0):
                    q.append(i)
        
        return n==nvis
        