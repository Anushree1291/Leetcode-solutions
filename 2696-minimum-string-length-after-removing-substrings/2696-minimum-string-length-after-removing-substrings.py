from collections import deque
class Solution:
    def minLength(self, s: str) -> int:
        st=[]
        for i in range(len(s)):
            if len(st)==0:
                st.append(s[i])
            elif s[i]=="B" and st[-1]=="A" :
                st.pop()
            elif s[i] == "D" and st[-1]=="C":
                st.pop()
            else:
                st.append(s[i])
        return len(st)