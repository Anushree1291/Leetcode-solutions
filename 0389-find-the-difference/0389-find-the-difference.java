class Solution {
    public char findTheDifference(String s, String t) {
        if(s.length()==0){
            return t.charAt(0);
        }
        int a[]=new int[26];
        char c=' ';
        Arrays.fill(a,0);
        for(char ch:s.toCharArray()){
            a[ch-'a']++;
        }
        for(char ch:t.toCharArray()){
            --a[ch-'a'];
            if(a[ch-'a']==-1){
                c=ch;
            }
        }
        return c;
    }
}