class Solution {
    public boolean canConstruct(String r, String m) {
        int a[]=new int[26];
        Arrays.fill(a,0);
        boolean b=true;
        for(char ch:m.toCharArray()){
            a[ch-'a']++;
        }
        for(char ch:r.toCharArray()){
            if(--a[ch-'a']<0){
                b=false;
            }
        }
        return b;
    }
}