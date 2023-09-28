class Solution {
    public int[] sortArrayByParity(int[] n) {
        int z=n.length-1;
        int x=0;
        int s=0;
        while(x<z){
            while(x<z &&  n[z]%2!=0){
                z--;
            }
            if(x<n.length && z>=0 && n[x]%2!=0){
                s=n[z];
                n[z]=n[x];
                n[x]=s;
                x++;
                z--;
            }
            if(x<n.length && n[x]%2==0){
                x++;
            }
        }
        return n;
    }
}