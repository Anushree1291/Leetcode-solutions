//{ Driver Code Starts
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while(t-- > 0){
            
            int n;
            n = Integer.parseInt(br.readLine());
            
            Solution obj = new Solution();
            int res = obj.findCatalan(n);
            
            System.out.println(res);
            
        }
    }
}

// } Driver Code Ends



class Solution {
    public static int findCatalan(int n) {
        // code here
        if(n==0||n==1)
            return 1;
        int a[]=new int[n+1];
        a[0]=1;
        a[1]=1;
        int ans=0;
        int mod= (int)1e9 + 7;
        for(int i=2;i<=n;i++){
            int k=i-1;
            for(int j=0;j<i;j++){
                a[i]=(a[i]+(int)((long)a[j]*a[k]%mod))%mod;
                k--;
            }
        }
        return a[n];
    }
}
        
