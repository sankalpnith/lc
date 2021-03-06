# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        level = [root]
        output = []
        reverse = True 
        while level:
            curr_level, next_level = [], []
        
            for node in level:
                curr_level.append(node.val)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            
            # Starts ===> This section is for spiral order print
            if reverse: 
                print(curr_level[::-1])
            else:
                print(curr_level)
            reverse = not reverse
            # Ends ====> This section is for spiral order print
            
            output.append(curr_level)
            level = next_level
        
        return output[::-1]
