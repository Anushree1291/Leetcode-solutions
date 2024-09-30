class CustomStack {
    int top;
    int arr[];
    int max;

    public CustomStack(int maxSize) {
        top=-1;
        arr=new int[maxSize];
        max=maxSize;
    }
    
    public void push(int x) {
        if(top!=max-1){
            arr[++top]=x;
        }
    }
    
    public int pop() {
        if(top!=-1)
            return arr[top--];
        else
            return -1;
    }
    
    public void increment(int k, int val) {
        if(k>top){
            k=top+1;
        }
        for(int i=0;i<k;i++){
                 arr[i]=arr[i]+val;
            }
        
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */