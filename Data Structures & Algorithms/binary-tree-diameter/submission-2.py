# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        # The longest diameter does not have to go through the root 
        # res denotes the longest diameter found in the tree
        # res can be greater the diameter calculated at the root

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, left+right)

            return 1 + max(left,right)
        
        dfs(root)
        return(self.res)