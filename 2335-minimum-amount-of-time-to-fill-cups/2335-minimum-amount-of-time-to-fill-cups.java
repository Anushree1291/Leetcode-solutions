import java.util.PriorityQueue;
class Solution {
    public int fillCups(int[] a) {
        PriorityQueue<Integer> q = new PriorityQueue<>();
        for(int i:a){
            q.add(-1*i);
        }
        int t=0;
        while (q.peek()!=0){
            int x=-1*q.poll();
            int y=-1*q.poll();
            t+=1;
            q.add(-1*(x-1));
            q.add(-1*(y-1));
            
        }
        return t;
    }
}