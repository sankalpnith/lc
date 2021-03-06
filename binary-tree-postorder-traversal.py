# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack, output_stack = [] , []
        if root is None: return output_stack
        stack = [root]
        while stack:
            node = stack.pop()
            output_stack.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        
        # pop from output_stack and store in output....
        return output_stack[::-1] 
