#User function Template for python3
class Solution:
	def isPalindrome(self, s):
		# code here
		l=0
		h=len(s)-1
		while (l<h):
		    if s[l]!=s[h]:
		        return 0
		    l+=1
		    h-=1
		return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends