# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        visited = []

        while root:

            if root.left:
                self.invertTree(root.left)

            if root.right:
                self.invertTree(root.right)

            temp = root.left
            root.left = root.right
            root.right = temp

            return root



        # while root:
        #     if root in visited:
        #         root = visited[-1]
        #     else:
        #         if root.left != None:
        #             temp = root.right
        #             root.right = root.left
        #             root.left = temp
                    


                

