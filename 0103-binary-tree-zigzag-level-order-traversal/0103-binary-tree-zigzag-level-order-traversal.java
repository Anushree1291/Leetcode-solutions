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
    public List<List<Integer>> zigzagLevelOrder(TreeNode r) {
        List<List<Integer>> result=new LinkedList();
        if(r==null){
            return result;
        }
        Queue<TreeNode> ar=new LinkedList<>();
        int l=0;
        ar.add(r);
        while(!ar.isEmpty()){
            List<Integer> arr=new LinkedList<Integer>();
            int a=ar.size();
            for(int i=0;i<a;i++){
                TreeNode t=ar.poll();
                if(t.left!=null){
                    ar.add(t.left);
                }
                if(t.right!=null){
                    ar.add(t.right);
                }
                if(l%2==0){
                    arr.add(t.val);
                }
                else{
                    arr.add(0,t.val);
                }
            }
            l++;
            result.add(arr);
        }
        return result;
    }
}