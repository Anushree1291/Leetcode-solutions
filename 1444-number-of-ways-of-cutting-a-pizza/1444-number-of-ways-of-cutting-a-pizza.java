class Solution {
    
    int a[][];
    Map<String,Integer> ar=new HashMap<String,Integer>();
    
    public int ways(String[] p, int k) {
        a=new int[p.length+1][p[0].length()+1];
        for(int i=0;i<p.length;i++){
            a[i][p[0].length()]=0;
        }
        Arrays.fill(a[p.length],0);
        for(int i=p.length-1;i>=0;i--){
            for(int j=p[0].length()-1;j>=0;j--){
                int c=0;
                if(p[i].charAt(j)=='A'){
                    c=1;
                }
                a[i][j]= a[i+1][j]+a[i][j+1]-a[i+1][j+1]+c;
                
            }
        }
        for(int i=0;i<p.length+1;i++){
            for(int j=0;j<p[0].length()+1;j++){
                System.out.print(a[i][j]);
                
            }System.out.println();}
        
        return tra(0,0,k-1);
    }
    int tra(int r,int c,int k){
        String s=r+" "+c+" "+k;
        if(ar.containsKey(s)) return ar.get(s);
        if(a[r][c]==0){
            return 0;
        }
        if(k==0) return 1;
        int ans =0;
        for(int i=r+1;i<a.length;i++){
            if((a[r][c]-a[i][c])>0){
                ans+=tra(i,c,k-1);
                ans=ans%1000000007;
            }
        }
        for( int j=c+1;j<a[0].length;j++){
            if(a[r][c]-a[r][j]>0){
                ans+=tra(r,j,k-1);
                ans=ans%1000000007;
            }
        }
        //ans=ans%1000000007;
        ar.put(s,ans);
        return ans%1000000007;
    }
    
}