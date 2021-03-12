# coding=utf-8
class Solution(object):
	def invertTree(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		# 递归函数的终止条件，节点为空时返回
		if not root:
			return None
		# 将当前节点的左右子树交换
		root.left,root.right = root.right,root.left
		# 递归交换当前节点的 左子树和右子树
		self.invertTree(root.left)
		self.invertTree(root.right)
		# 函数返回时就表示当前这个节点，以及它的左右子树
		# 都已经交换完了
		return root


        def invertTree2(self, root):
            """
            :type root: TreeNode
            :rtype: TreeNode
            """
            if not root:
                return None
            # 将二叉树中的节点逐层放入队列中，再迭代处理队列中的元素
            queue = [root]
            while queue:
                # 每次都从队列中拿一个节点，并交换这个节点的左右子树
                tmp = queue.pop(0)
                tmp.left, tmp.right = tmp.right, tmp.left
                # 如果当前节点的左子树不为空，则放入队列等待后续处理
                if tmp.left:
                    queue.append(tmp.left)
                # 如果当前节点的右子树不为空，则放入队列等待后续处理
                if tmp.right:
                    queue.append(tmp.right)
            # 返回处理完的根节点
            return root



if __name__ == '__main__':
    obj = Solution()
    root = [4,2,7,1,3,6,9]
    print obj.invertTree(root)