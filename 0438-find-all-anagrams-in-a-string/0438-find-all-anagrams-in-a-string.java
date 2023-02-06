class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        if(s.length()<p.length()) return new LinkedList<Integer>();
        Map<Character,Integer> as=new HashMap<Character,Integer>();
        Map<Character,Integer> ap=new HashMap<Character,Integer>();
        List<Integer>  ar=new LinkedList<Integer>();
        for(char ch:p.toCharArray()){
            ap.put(ch,ap.getOrDefault(ch,0)+1);
        }
        for(int i=0;i<p.length();i++){
            char ch=s.charAt(i);
            as.put(ch,as.getOrDefault(ch,0)+1);
        }
        if(as.equals(ap)){
            ar.add(0);
        }
        for(int i=1;p.length()+i<=s.length();i++){
            char ch=s.charAt(i-1);
            as.put(ch,as.get(ch)-1);
            if(as.get(ch)==0){
                as.remove(ch);
            }
            ch=s.charAt(p.length()+i-1);
            as.put(ch,as.getOrDefault(ch,0)+1);
            System.out.println(as);
            if(as.equals(ap)){
                ar.add(i);
            }
        }
        return ar;
    }
}