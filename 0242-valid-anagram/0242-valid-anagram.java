class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length()){
            return false;
        }
        int [] a=new int[26];
        Arrays.fill(a,0);
        for(char ch:s.toCharArray()){
            a[ch-'a']++;
        }
        for(int i=0;i<t.length();i++){
            a[t.charAt(i)-'a']--;
            if(a[t.charAt(i)-'a']<0){
                return false;
            }
        }
        return true;
    }
}