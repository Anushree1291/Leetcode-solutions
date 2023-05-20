class Solution:
    def calcEquation(self, eq: List[List[str]], val: List[float], qu: List[List[str]]) -> List[float]:
        m=collections.defaultdict(dict)
        for (x,y),v in zip(eq,val):
            m[x][y]=v
            m[y][x]=1/v
            
        def bfs(st,dt):
            if not( st in m and dt in m): return -1.0
            q,seen=[(st,1.0)],set()
            for x,v in q:
                if x==dt:
                    return v
                seen.add(x)
                for y in m[x]:
                    if y not in seen:
                        q.append((y,(v*m[x][y])))
            return -1.0
        return [bfs(s,d) for s,d in qu]