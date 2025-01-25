class Solution:
    def lexicographicallySmallestArray(self, n: List[int], l: int) -> List[int]:
        ns=sorted(n)
        c=0
        ng={}
        ng[ns[0]]=c

        gl={}
        gl[c]=deque([ns[0]])

        for i in range(1,len(n)):
            if abs(ns[i] - ns[i-1]) > l:
                c+=1
            ng[ns[i]]=c

            if c not in gl:
                gl[c]=deque()
            gl[c].append(ns[i])

        for i in range(len(n)):
            nu=n[i]
            g=ng[nu]
            n[i]=gl[g].popleft()
        
        return n