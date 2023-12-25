#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, a):
        #Code here
        dp={}
        s=0
        m=0
        for i in range(len(a)):
            if a[i]==0:
                m=max(m,1)
            s+=a[i]
            if s==0:
                m=max(m,i+1)
            if s in dp:
                m=max(m,i-dp[s])
            else:
                dp[s]=i
        return m
        


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends