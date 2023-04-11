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
    boolean b=true;
    public boolean isSymmetric(TreeNode r) {
        b=traversal(r.right,r.left);
        return b;
    }
    public boolean traversal(TreeNode r,TreeNode l){
        if(r==null || l==null){
            return r==l;
        }
        if(r.val!=l.val){
            return false;
        }
        return traversal(r.right,l.left) && traversal(r.left,l.right);
    }
}