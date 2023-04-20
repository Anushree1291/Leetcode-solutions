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
    int m;
    Map<Integer,Integer> ar;
    public int widthOfBinaryTree(TreeNode root) {
        m=0;
        ar=new HashMap<>();
        ar.put(0,0);
        traversal(root,0,0);
        return m;
    }
    public void traversal(TreeNode root,int depth,int position){
        if(root==null){
            return;
        }
        ar.computeIfAbsent(depth,x->position);
        m=Math.max(m,position-ar.get(depth)+1);
        traversal(root.left,depth+1,position*2);
        traversal(root.right,depth+1,position*2+1);
    }
}