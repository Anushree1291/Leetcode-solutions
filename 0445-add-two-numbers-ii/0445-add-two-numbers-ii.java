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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
       l1=reverse(l1);
        l2=reverse(l2);
        int c=0;
        ListNode a,b=new ListNode(-1);
        a=b;
        int s=0;
         while(l1!=null || l2!=null){
            s=0;
            if(l2==null){
                s+=l1.val+c;
                l1=l1.next;
            }
            else if(l1==null){
                s+=l2.val+c;
                l2=l2.next;
            }
            else{
                s+=l2.val+l1.val+c;
                l2=l2.next;
                l1=l1.next;
            }
            if(s>=10){
                c=s/10;
                s=s%10;
            }
            else{
                c=0;
            }
            //System.out.println(s);
            b.next=new ListNode(s);
            b=b.next;
        }
        if(c==1){
            b.next=new ListNode(c);
        }
        return reverse(a.next);
    }
    public ListNode reverse(ListNode a){
        ListNode b,c,d;
        b=null;
        c=a;
        d=a;
        while(c!=null){
            d=d.next;
            c.next=b;
            b=c;
            c=d;
        }
        return b;
    }
}