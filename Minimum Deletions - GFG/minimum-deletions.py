#User function Template for python3

class Solution:
    def minimumNumberOfDeletions(self,s):
        # code here 
        n=len(s)
        a=s[::-1]
        L = [[0]*(n+1) for i in range(n+1)]
 
    # Following steps build L[m+1][n+1] in bottom up fashion
    # Note: L[i][j] contains length of LCS of X[0..i-1]
    # and Y[0..j-1]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if a[i-1] == s[j-1]:
                    L[i][j] = L[i-1][j-1]+1
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])
     
        # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
        return n-L[n][n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends