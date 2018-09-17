# 建两个list
# nodelist存放节点
# vallist存放节点值
# nodelist中，每次弹出list最前面的节点，append节点值到vallist中，
# 同时将此节点的左右孩子append到nodelist中
class BinaryTree:
	def __init__(self, root):
		self.key = root
		self.leftChild = None
		self.rightChild = None

def levelPrint(root):
    if not root:
        return []
    nodelist = []
    vallist = []
    nodelist.append(root)
    while nodelist:
        node = nodelist.pop(0)
        vallist.append(node.key)
        if node.leftChild:
            nodelist.append(node.leftChild)
        if node.rightChild:
            nodelist.append(node.rightChild)
    return vallist


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

# def levelPrint(root):
#     if not root:
#         return []
#     nodelist = []
#     vallist = []
#     nodelist.append(root)
#     while nodelist:
#         node = nodelist.pop(0)
#         vallist.append(node.key)
#         if node.leftChild:
#             nodelist.append(node.leftChild)
#         if node.rightChild:
#             nodelist.append(node.rightChild)
#     return vallist


# preorder = [8, 6, 5, 7, 10, 9, 11]
# inorder = [5, 6, 7, 8, 9, 10, 11]
# r = reConstructBinaryTree(preorder, inorder)

# print(levelPrint(r))
