# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
# https://www.geeksforgeeks.org/print-nodes-distance-k-given-node-binary-tree/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        ans = []
        def dfs(node):
            # This method returns distance between node and target
            if node is None:
                return -1
            if node is target:
                subtree_add(node, 0)
                return 1
            
            # Check if target exists in left side, get distance of left child to target in L
            # if L is K that means root is at K distance from target, append it to ans
            # else check for root's right child for distance K-L+1 
            # return L+1 for root's parent..
            L = dfs(node.left)
            if L != -1:
                if L == K:
                    ans.append(node.val)
                else:
                    subtree_add(node.right, L+1)
                    return L+1
            
            R = dfs(node.right)
            
            if R != -1:
                if R == K:
                    ans.append(node.val)
                else:
                    subtree_add(node.left, R+1)
                    return R+1
            
            return -1
        
        def subtree_add(node, dist):
            if node is None: 
                return
            if dist == K:
                ans.append(node.val)
            subtree_add(node.left, dist+1)
            subtree_add(node.right, dist+1)
        
        dfs(root)
        return ans
        
                
                
