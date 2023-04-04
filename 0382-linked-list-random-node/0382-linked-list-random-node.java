/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode h;
    
    public Solution(ListNode head) {
        this.h=head;
    }
    
    public int getRandom() {
        int x=1;
        int r=0;
        ListNode c=this.h;
        while(c!=null){
            if(Math.random()<(1.0/x)){
                r=c.val;
            }
            x++;
            c=c.next;
        }
        return r;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */