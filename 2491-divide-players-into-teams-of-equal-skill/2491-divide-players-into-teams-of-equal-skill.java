class Solution {
    public long dividePlayers(int[] s) {
        if(s.length==2){
            return (long)(s[0]*s[1]);
        }
        if(s.length%2!=0){
            return -1;
        }
        int sk=0;
        for(int i:s){
            sk+=i;
        }
        if((sk*2)%s.length!=0){
            return -1;
        }
        sk=(int)((sk*2)/s.length);
        int a=s.length;
        long su=0;
        //System.out.println(sk);
        Arrays.sort(s);
        for(int i=0;i<s.length/2;i++){
            if(s[i]+s[a-1-i]==sk){
                su+=s[i]*s[a-1-i];
            }
            else{
                return -1;
            }
        }
        return su;
    }
}