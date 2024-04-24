class Solution {
    public int tribonacci(int n) {
        if(n==0){
            return 0;
        }
        else if(n==1){
            return 1;
        }
        else if(n==2){
            return 1;
        }
        else if(n==3){
            return 2;
        }
        else{
            int n0=0;
            int n1=1;
            int n2=1;
            int nend=0;
            for(int i=2;i<n;i++){
                nend=n0+n1+n2;
                n0=n1;
                n1=n2;
                n2=nend;
            }
            return nend;
        }
    }
    
}