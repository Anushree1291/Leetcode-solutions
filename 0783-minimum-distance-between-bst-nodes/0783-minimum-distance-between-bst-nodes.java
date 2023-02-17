/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int r=Integer.MAX_VALUE ;
    TreeNode p=null;
    public int minDiffInBST(TreeNode root) {
        traversal (root);
        return r;
    }
    public void traversal(TreeNode ro){
        if(ro==null){
            return ;
        }
        traversal(ro.left);
        if(p!=null){
            r=Math.min(r,ro.val-p.val);
        }
        p=ro;
        traversal(ro.right);
    }
}