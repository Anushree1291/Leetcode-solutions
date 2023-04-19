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
    int m=0;
    public int longestZigZag(TreeNode r) {
        tra(r.left,0,1);
        tra(r.right,1,1);
        return m;
    }
    public void tra(TreeNode r,int d,int l){
        if(r==null){
            return;
        }
        m=Math.max(m,l);
        if(d==0){
            tra(r.left,0,1);
            tra(r.right,1,l+1);
        }
        else{
            tra(r.left,0,l+1);
            tra(r.right,1,1);
        }
    }
}