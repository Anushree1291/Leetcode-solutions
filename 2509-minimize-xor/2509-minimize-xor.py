class Solution:
    def minimizeXor(self, n1: int, n2: int) -> int:
        r=n1
        t=bin(n2).count("1")
        s=bin(n1).count("1")
        c=0

        while s<t :
            if not (r &(1<<c))!=0 :
                r= r|(1<<c)
                s+=1
            c+=1


        while s>t :
            if (r & (1<<c))!=0 :
                r= r& ~(1<<c)
                s-=1
            c+=1
        return r