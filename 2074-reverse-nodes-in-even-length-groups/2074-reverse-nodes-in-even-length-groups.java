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
    public ListNode reverseEvenLengthGroups(ListNode head) {
        return tra(head,1);
    }
    public ListNode tra(ListNode head,int k){
        
        if(head==null || head.next==null){
            return head;
        }
        ListNode a=head;
        ListNode d=head;
        int c=0;
        while(c!=k && a!=null){
            c++;
            a=a.next;
        }
        ListNode b=tra(a,k+1);
        if(c%2==0){
            while(c!=0){
                c--;
                b=new ListNode(d.val,b);
                d=d.next;
            }
            head=b;
            System.out.println(head.val);
        }
        else{
            while(c>1){
                c--;
                d=d.next;
            }
            d.next=b;
        }
        return head;
    }
}