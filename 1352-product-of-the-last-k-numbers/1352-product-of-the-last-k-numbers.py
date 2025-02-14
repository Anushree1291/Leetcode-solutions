class ProductOfNumbers:

    def __init__(self):
        self.c=0
        self.p=[]
        self.a=[]
        self.p.append(1)
        self.n=0
        

    def add(self, num: int) -> None:
        self.a.append(num)
        self.p.append(num*self.p[len(self.p)-1])
        if num==0:
            self.c=self.n
        self.n+=1

    def getProduct(self, k: int) -> int:
        if k>len(self.p)-self.c:
            return 0
        b=1
        for i in range(len(self.a)-k,len(self.a)):
            b*=self.a[i]
        return b


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)