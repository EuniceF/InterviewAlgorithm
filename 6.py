# 通过前序遍历(根左右)，可以得到root（前序遍历第一个元素）；
# 通过中序遍历(左根右)，root左半部分构成左子树，右半部分构成右子树。
# 递归
class BinaryTree:
	def __init__(self, root):
		self.key = root
		self.leftChild = None
		self.rightChild = None

	def preordertree(self):
		print(self.key)
		if self.leftChild:
			self.leftChild.preordertree()
		if self.rightChild:
			self.rightChild.preordertree()

	def inordertree(self):
		if self.leftChild:
			self.leftChild.inordertree()
		print(self.key)
		if self.rightChild:
			self.rightChild.inordertree()


def reConstructBinaryTree(preorder, inorder):
	if len(preorder) != len(inorder):
		return 
	if not preorder or not inorder:
		return

	root = BinaryTree(preorder[0])
	index = inorder.index(root.key)
	
	root.leftChild = reConstructBinaryTree(preorder[1: index + 1], inorder[: index])
	root.rightChild = reConstructBinaryTree(preorder[index + 1:], inorder[index + 1:])
	return root


# test
preorder = [1, 2, 4, 7, 3, 5, 6, 8]
inorder = [4, 7, 2, 1, 5, 3, 8, 6]
r = reConstructBinaryTree(preorder, inorder)

print('Preorder is: ')
r.preordertree()
print('Inorder is: ')
r.inordertree()
