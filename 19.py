class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

# 遍历树，交换左右孩子
def mirror(root):
    if not root or root.leftChild == None or root.rightChild == None:
        return root
    root.leftChild, root.rightChild = root.rightChild, root.leftChild
    mirror(root.leftChild)
    mirror(root.rightChild)
    return root




# # for test
# class BinaryTree:
# 	def __init__(self, root):
# 		self.key = root
# 		self.leftChild = None
# 		self.rightChild = None

# 	def preordertree(self):
# 		print(self.key)
# 		if self.leftChild:
# 			self.leftChild.preordertree()
# 		if self.rightChild:
# 			self.rightChild.preordertree()

# 	def inordertree(self):
# 		if self.leftChild:
# 			self.leftChild.inordertree()
# 		print(self.key)
# 		if self.rightChild:
# 			self.rightChild.inordertree()


# def reConstructBinaryTree(preorder, inorder):
# 	if len(preorder) != len(inorder):
# 		return 
# 	if not preorder or not inorder:
# 		return

# 	root = BinaryTree(preorder[0])
# 	index = inorder.index(root.key)
	
# 	root.leftChild = reConstructBinaryTree(preorder[1: index + 1], inorder[: index])
# 	root.rightChild = reConstructBinaryTree(preorder[index + 1:], inorder[index + 1:])
# 	return root

# def mirror(root):
#     if not root or root.leftChild == None or root.rightChild == None:
#         return root
#     root.leftChild, root.rightChild = root.rightChild, root.leftChild
#     mirror(root.leftChild)
#     mirror(root.rightChild)
#     return root


# preorder = [8, 6, 5, 7, 10, 9, 11]
# inorder = [5, 6, 7, 8, 9, 10, 11]
# r = reConstructBinaryTree(preorder, inorder)

# mirror_r = mirror(r)
# print('Preorder is: ')
# mirror_r.preordertree()
# print('Inorder is: ')
# mirror_r.inordertree()