class Solution:
    def islandPerimeter(self, g: List[List[int]]) -> int:
        
        def tra(i,j):
            if i<0 or j<0 or i>len(g)-1 or j>len(g[0])-1 or g[i][j]==0:
                return 1
            elif self.b[i][j]==False:
                return 0
            a=0
            self.b[i][j]=False
            a+=tra(i-1,j)
            a+=tra(i,j-1)
            a+=tra(i+1,j)
            a+=tra(i,j+1)
            return a



        self.b=[[[False] for _ in range(len(g[0]))]for _ in range(len(g))]
        a,b=0,0
        for i in range(len(g)):
            for j in range(len(g[i])):
                if g[i][j]==1:
                    a,b=i,j
                    self.b[i][j]=True
        return tra(a,b)