Leetcode question - 1470. Shuffle the Array
https://leetcode.com/problems/shuffle-the-array

class Solution {
    public int[] shuffle(int[] nu, int n) {
        int a,l;
        a=nu.length/2;
        l=0;
        int an[]=new int[nu.length];
        for(int i=0;i<nu.length;i++){
            if(i%2==0){
                an[i]=nu[l];
            }
            else{
                an[i]=nu[l+a];l++;
            }
        }
        return an;
    }
}
