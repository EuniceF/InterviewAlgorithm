class BinaryTree:
	def __init__(self, root):
		self.key = root
		self.leftChild = None
		self.rightChild = None

# # dfs深度优先遍历
# def binaryTreePath(root):
#     if not root:
#         return []
#     res = []
#     dfs(root, res, '' + str(root.key))
#     return res

# def dfs(root, res, path):
#     if root.leftChild == None and root.rightChild == None:
#         res.append(path)
#     if root.leftChild != None:
#         dfs(root.leftChild, res, path + '->' + str(root.leftChild.key))
#     if root.rightChild != None:
#         dfs(root.rightChild, res, path + '->' + str(root.rightChild.key))


def findPath(root, target):
    if not root:
        return []
    res = []
    dfs(root, res, [root.key], target) #先把root值加进去
    return res

def dfs(root, res, path, target):
    if root.leftChild == None and root.rightChild == None and sum(path) == target:
        res.append(path)
    if root.leftChild != None:
        dfs(root.leftChild, res, path + [root.leftChild.key], target)
    if root.rightChild != None:
        dfs(root.rightChild, res, path + [root.rightChild.key], target)
    


