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
    List<Integer> ar;
    public boolean findTarget(TreeNode root, int k) {
        ar=new LinkedList();
        return tra(root,k);
    }
    public boolean tra(TreeNode r,int k){
        if(r==null){
            return false;
        }
        if(ar.contains(r.val)){
            return true;
        }
        boolean b;
        ar.add(k-r.val);
        b=tra(r.left,k);
        if(b){
            return true;
        }
        b=tra(r.right,k);
        if(b){
            return true;
        }
        return false;
    }
}