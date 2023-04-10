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
    public ListNode removeElements(ListNode head, int val) {
        if(head==null){
            return null;
        }
        ListNode p=new ListNode(-1),q;
        q=p;
        while( head!=null){
            if(head.val!=val){
                p.next=new ListNode(head.val);
                p=p.next;
            }
            head=head.next;
        }
        return q.next;
    }
}