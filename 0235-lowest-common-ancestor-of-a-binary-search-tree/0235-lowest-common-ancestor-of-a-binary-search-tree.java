/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode r, TreeNode p, TreeNode q) {
        int min=Math.min(p.val,q.val);
        int max=Math.max(p.val,q.val);
        while(r!=null){
            int c=r.val;
            if(min <r.val && max<r.val){
                r=r.left;
            }
            else if(min >r.val && max>r.val){
                r=r.right;
            }
            else{
                break;
            }
        }
        return r;
    }
}