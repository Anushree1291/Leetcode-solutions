class Solution {
    public int[] minOperations(String b) {
        int answer[]=new int[b.length()];
        char c[]=b.toCharArray();
        for(int i=0;i<b.length();i++){
            int j=0;int k=0;
            for(char ch:c){
                j+=Character.getNumericValue(ch)*Math.abs(i-k);
                k++;
            }
            answer[i]=j;
        }
        return answer;
    }
}