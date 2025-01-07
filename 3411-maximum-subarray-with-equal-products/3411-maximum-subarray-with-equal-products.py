class Solution:
    def maxLength(self, n: List[int]) -> int:
        m=1
        for i in range(len(n)):
            for j in range(i,len(n)):
                a=n[i:j+1]
                g=reduce(math.gcd,a)
                l=reduce(math.lcm,a)
                p=math.prod(a)
                if p==g*l:
                    m=max(len(a),m)
        return m