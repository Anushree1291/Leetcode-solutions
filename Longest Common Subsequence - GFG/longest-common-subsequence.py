#User function Template for python3

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        
        # code here
        a=[[0]*(x+1) for _ in range(y+1)]
        
        for i in range(1,y+1):
            for j in range(1,x+1):
                if s2[i-1]==s1[j-1]:
                    a[i][j]=a[i-1][j-1]+1
                else:
                    a[i][j]=max(a[i-1][j],a[i][j-1])
        
        
        return a[y][x]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        x,y = map(int,input().strip().split())
        s1 = str(input())
        s2 = str(input())
        ob=Solution()
        print(ob.lcs(x,y,s1,s2))
# } Driver Code Ends