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
    public ListNode reverseKGroup(ListNode head, int k) {
        if(head==null || head.next==null || k==1){
            return head;
        }
        ListNode a=head;
        ListNode d=head;
        int c=0;
        while(c!=k && a!=null){
            c++;
            a=a.next;
        }
        if(c==k){
            a=reverseKGroup(a,k);
            while(c!=0){
                c--;
                a=new ListNode(d.val,a);
                d=d.next;
            }
            head=a;
        }
        return head;
    }
}