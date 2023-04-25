class SmallestInfiniteSet {
    PriorityQueue<Integer> ar;
    int m;

    public SmallestInfiniteSet() {
        m=1;
        ar=new PriorityQueue<>();
    }
    
    public int popSmallest() {
        if(!ar.isEmpty() && m==ar.peek()){
            m++;
            ar.poll();
            return m-1;
        }
        else if(!ar.isEmpty() && m>ar.peek()){
            return ar.poll();
        }
        m++;
        return m-1;
    }
    
    public void addBack(int num) {
        if(num>=m || ar.contains(num)){
            return;
        }
        ar.add(num);
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.popSmallest();
 * obj.addBack(num);
 */