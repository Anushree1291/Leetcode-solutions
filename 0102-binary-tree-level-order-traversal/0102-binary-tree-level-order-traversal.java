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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> arr=new LinkedList<>();
        if(root==null) {
            return arr;
        }
        Queue<TreeNode> q=new LinkedList<TreeNode>();
        q.add(root);
        
        while (!q.isEmpty()){
            List<Integer> ar=new LinkedList<>();
            int a=q.size();
            while (a!=0){
                a--;
                TreeNode c=q.poll();
                ar.add(c.val);
                if(c.left!=null){
                    q.add(c.left);
                }
                if(c.right!=null){
                    q.add(c.right);
                }
            }
            arr.add(new LinkedList<>(ar));
            ar.clear();
        }
        return arr;
    }
}