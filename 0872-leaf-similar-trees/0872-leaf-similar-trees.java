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
    public boolean leafSimilar(TreeNode r1, TreeNode r2) {
        return tra(r1).equals(tra(r2));
    }
    public String tra(TreeNode r){
        String s="";
        if(r.left==null && r.right==null){
            s+=Integer.toString(r.val)+" ";
            return s;
        }
        if(r.left!=null){
            s+=tra(r.left);
        }
        if(r.right!=null){
            s+=tra(r.right);
        }
        return s;
    }
}