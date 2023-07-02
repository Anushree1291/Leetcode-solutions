class Solution:
    def maximumRequests(self, n: int, r: List[List[int]]) -> int:
        self.a=0
        
        def tra(ind,c):
            #print(ind)
            if(ind>=len(r)):
                for i in range(n):
                    if inx[i]!=0:
                        return;
                self.a=max(self.a,c)
                return
            
            tra(ind+1,c)
            
            inx[r[ind][0]]-=1
            inx[r[ind][1]]+=1
            tra(ind+1,c+1)
            
            inx[r[ind][0]]+=1
            inx[r[ind][1]]-=1
            
            return
        
        
        inx=[0]*n
        tra(0,0)
        return self.a