class Solution {
    public char nextGreatestLetter(char[] l, char t) {
        int i=0;
        for(i=0;i<l.length;i++){
            if(t<l[i]){
                break;
            }
        }
        if(i==l.length){
            i=0;
        }
        return l[i];
    }
}