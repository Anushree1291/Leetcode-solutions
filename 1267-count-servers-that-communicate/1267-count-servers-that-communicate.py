class Solution:
    def countServers(self, g: List[List[int]]) -> int:
        r=[0 for _ in range(len(g))]
        c=[0 for _ in range(len(g[0]))]
        for i in range(len(g)):
            co=0
            for j in range(len(g[0])):
                if g[i][j]==1 :
                    co+=1
            r[i]=co
        for i in range(len(g[0])):
            co=0
            for j in range(len(g)):
                if g[j][i]==1 :
                    co+=1
            c[i]=co
        co=0
        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j]==1:
                    if r[i] >1 or c[j]>1:
                        co+=1
        return co