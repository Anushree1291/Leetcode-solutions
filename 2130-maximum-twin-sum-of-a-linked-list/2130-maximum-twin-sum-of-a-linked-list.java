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
    public int pairSum(ListNode head) {
        ListNode a=head,b=head;
        while(b!=null){
            b=b.next.next;
            a=a.next;
        }
        System.out.println(a.val);
        ListNode c=a;
        int m=Integer.MIN_VALUE;
        b=head;
        a=null;
        while(c!=null){
            a=new ListNode(c.val,a);
            c=c.next;
        }
        while(a!=null){
            m=Math.max(m,(a.val+b.val));
            a=a.next;
            b=b.next;
        }
        return m;
    }
}