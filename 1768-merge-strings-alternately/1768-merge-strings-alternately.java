class Solution {
    public String mergeAlternately(String w1, String w2) {
        String s="";
        int i=0;
        int j=0;
        while(i<w1.length() && j<w2.length()){
            s=s+w1.charAt(i)+w2.charAt(j);
            i++;
            j++;
        }
        if(i<w1.length()){
            s+=w1.substring(i);
        }
        if(j<w2.length()){
            s+=w2.substring(j);
        }
        return s;
    }
}