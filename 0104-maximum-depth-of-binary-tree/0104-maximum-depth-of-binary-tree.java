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
    int max=0;
    int c=0;
    public int maxDepth(TreeNode root) {
        if(root==null){
            return c;
        }
        traversal(root);
        return max;
    }
    public void traversal(TreeNode r){
        ++c;
        max=Math.max(c,max);
        if(r.left!=null){
            System.out.println(r.val+" "+c);
            traversal(r.left);
            --c;
        }
        if(r.right!=null){
            System.out.println(r.val+" "+c);
            traversal(r.right);
            --c;
        }
    }
}