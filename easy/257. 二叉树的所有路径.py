# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def demo(root, path):
            if root:
                path += str(root.val)
                if not root.right and not root.left:
                    paths.append(path)
                else:
                    path += '->'
                    demo(root.left, path)
                    demo(root.right, path)
        paths = []
        demo(root, '')
        return paths