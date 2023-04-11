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
    List<Integer> ar=new ArrayList<Integer>();
    public List<Integer> preorderTraversal(TreeNode r) {
        if(r==null){
            return ar;
        }
        ar.add(r.val);
        preorderTraversal(r.left);
        preorderTraversal(r.right);
        return ar;
    } 
}