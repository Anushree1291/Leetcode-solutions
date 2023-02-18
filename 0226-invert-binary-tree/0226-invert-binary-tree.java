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
    public TreeNode invertTree(TreeNode r) {
        if(r==null){
            return null;
        }
        TreeNode le=invertTree(r.left);
        TreeNode ri=invertTree(r.right);
        r.left=ri;
        r.right=le;
        return r;
    }
}