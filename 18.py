class BinaryTree:
	def __init__(self, root):
		self.key = root
		self.leftChild = None
		self.rightChild = None


# 判断child是否为parent的子树或完全相等
def doseParentHaveChild(parent, child):
    # 如果child为空，则一定是parent的子树
    if child == None:
        return True
    # 比较节点值
    if not parent or parent.key != child.key:
        return False
    # 递归比较左子树右子树
    return doseParentHaveChild(parent.leftChild, child.leftChild) and doseParentHaveChild(parent.rightChild, child.rightChild)

# 查找parent中是否存在child的根节点
def hasSubTree(parent, child):
	if child == None or parent == None:
		return False
	return doseParentHaveChild(parent, child) or hasSubTree(parent.leftChild, child) or hasSubTree(parent.rightChild, child)

