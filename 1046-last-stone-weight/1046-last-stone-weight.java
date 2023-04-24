class Solution {
    public int lastStoneWeight(int[] s) {
        PriorityQueue<Integer> ar =new PriorityQueue<>((x,y)->y-x);
        for( int i : s){
            ar.add(i);
            
        }
        while(ar.size()!=1 && !ar.isEmpty()){
            int a=ar.poll();
            int b=ar.poll();
            if(a!=b)
                ar.add(a-b);
        }
        if(!ar.isEmpty()){
            return ar.poll();
        }
        return 0;
    }
}