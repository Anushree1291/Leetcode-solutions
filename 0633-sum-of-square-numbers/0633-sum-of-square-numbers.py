class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        m=[]
        for i in range(0,int(math.sqrt(c)+1)):
            if c-i*i in m:
                return True
            if c==2*i*i:
                return True
            m.append(i*i)
        return False