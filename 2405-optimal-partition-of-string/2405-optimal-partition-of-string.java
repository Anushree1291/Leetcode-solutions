class Solution {
    public int partitionString(String s) {
        Set<Character> ar=new HashSet<>();
        int ans=0;
        for(int i=0;i<s.length();i++){
            int a=ar.size();
            ar.add(s.charAt(i));
            int b=ar.size();
            if(a==b){
                ans++;
                ar.clear();
                ar.add(s.charAt(i));
            }
            ar.add(s.charAt(i));
        }
        return ans+1;
    }
}