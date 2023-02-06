class Solution {
    public String getHint(String s, String g) {
        int a[]=new int[10];
        for(char ch:s.toCharArray()){
            a[ch-'0']++;
        }
        int b=0,c=0;
        for(int i=0;i<g.length();i++){
            if(g.charAt(i)==s.charAt(i)){
                b++;
                a[g.charAt(i)-'0']--;
            }
        }
        for(int i=0;i<g.length();i++){
            if(g.charAt(i)!=s.charAt(i) && s.indexOf(g.charAt(i))!=-1 && a[g.charAt(i)-'0']>0){
                c++;
                a[g.charAt(i)-'0']--;
            }
        }
        String sc=b+"A"+c+"B";
        return sc;
    }
}