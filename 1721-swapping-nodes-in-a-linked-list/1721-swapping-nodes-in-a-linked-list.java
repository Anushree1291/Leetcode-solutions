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
    public ListNode swapNodes(ListNode head, int k) {
        ListNode a=head;
        int c=0;
        int ar[]=new int[100001];
        while(a!=null){
            ar[c]=a.val;
            c++;
            a=a.next;
        }
        System.out.println(c);
        int t=ar[k-1];
        ar[k-1]=ar[c-k];
        ar[c-k]=t;
        a=head;
        c=0;
        while(a!=null){
            a.val=ar[c];
            c++;
            a=a.next;
        }
        return head;
    }
}