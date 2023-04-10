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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if(l1==null){
            return l2;
        }
        else if(l2==null){
            return l1;
        }
        ListNode a,b=new ListNode(-1);
        a=b;
        while(l1!=null && l2!=null){
            if(l1!=null && l1.val<=l2.val){
                b.next=new ListNode(l1.val);
                l1=l1.next;
                b=b.next;
            }
            else if(l2!=null && l1.val>l2.val){
                b.next=new ListNode(l2.val);
                l2=l2.next;
                b=b.next;
            }
            
        }
        while(l1!=null){
            b.next=new ListNode(l1.val);
                l1=l1.next;
                b=b.next;
        }
        while(l2!=null){
            b.next=new ListNode(l2.val);
                l2=l2.next;
                b=b.next;
        }
        return a.next;
    }
}