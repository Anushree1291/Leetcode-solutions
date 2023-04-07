class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> ar=new HashMap<>();
        for(int i=0;i<s.length();i++){
            ar.put(s.charAt(i),ar.getOrDefault(s.charAt(i),0)+1);
        }
        for(int i=0;i<s.length();i++){
            if(ar.get(s.charAt(i))==1){
                return i;
            }
        }
        return -1;
    }
}