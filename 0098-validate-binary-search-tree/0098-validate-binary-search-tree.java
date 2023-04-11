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
    public boolean isValidBST(TreeNode root) {
        return tra(Long.MIN_VALUE,Long.MAX_VALUE,root);
    }
    public boolean tra(long l,long u,TreeNode r){
        if(r==null){
            return true;
        }
        else if(r.val<=l || r.val>=u){
            return false;
        }
        else{
            return tra(l,r.val,r.left) && tra(r.val,u,r.right);
        }
    }
}