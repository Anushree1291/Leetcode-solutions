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
    List<Integer> ar= new ArrayList<Integer>();
    public List<Integer> inorderTraversal(TreeNode root) {
        if(root==null){
            return ar;
        }
        traversal(root);
        return ar;
    }
    public void traversal(TreeNode r){
        if(r.left!=null){
           traversal(r.left);
        }
        ar.add(r.val);
        if(r.right!=null){
           traversal(r.right);
        }
    }
}