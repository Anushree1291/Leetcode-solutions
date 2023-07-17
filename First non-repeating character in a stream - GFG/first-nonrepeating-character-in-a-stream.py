#User function Template for python3
from collections import deque

class Solution:
	def FirstNonRepeating(self, a):
		# Code here
		q=deque()
		s=""
		c=[0]*26
		for i in a:
		    ind=ord(i)-ord("a")
		    q.append(i)
		    c[ind]+=1
		    #print(i,q[0])
		    while( q and c[ord(q[0])-ord("a")]>1):
		        q.popleft()
		    curr="#"
		    if q:
		        curr=q[0]
		    s+=curr
		#print( c)
		return s
		    
		        
		    
		

#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		A = input()
		ob = Solution()
		ans = ob.FirstNonRepeating(A)
		print(ans)

# } Driver Code Ends