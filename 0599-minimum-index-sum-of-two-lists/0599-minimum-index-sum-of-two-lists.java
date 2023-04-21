class Solution {
    public String[] findRestaurant(String[] l1, String[] l2) {
        Map<String,Integer> ar =new HashMap<>();
        for(int i=0;i<l1.length;i++){
            ar.put(l1[i],i);
        }
        List<String> a=new LinkedList<>();
        int m=Integer.MAX_VALUE;
        for(int i=0;i<l2.length;i++){
            if(ar.containsKey(l2[i])){
                if(i+ar.get(l2[i])<m){
                    a.clear();
                    a.add(l2[i]);
                    m=i+ar.get(l2[i]);
                }
                else if(i+ar.get(l2[i])==m){
                    a.add(l2[i]);
                }
            }
        }
        return a.toArray(new String[0]);
    }
}