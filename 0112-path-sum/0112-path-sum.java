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
    public boolean hasPathSum(TreeNode r, int t) {
        if(r==null){
            return false;
        }
        boolean b=false;
        b=traversal(b,r,0,t);
        return b;
    }
    
    public boolean traversal(boolean b,TreeNode r, int s,int t){
        if(r.left==null && r.right==null && s+r.val==t){
            return true;
        }
        
        if(r.left!=null && !b){
            b=traversal(b,r.left,s+r.val,t);
        }
        if(r.right!=null && !b){
            b=traversal(b,r.right,s+r.val,t);
        }
        return b;
    }
}