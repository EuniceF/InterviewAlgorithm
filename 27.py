# Reference: https://blog.csdn.net/u010005281/article/details/79657259
class Solution:
    def __init__(self):
        self.listHead = None
        self.listTail = None

    def Convert(self, pNode):
        if pNode == None:
            return
        self.Convert(pNode.left)
        if self.listHead == None:
            self.listHead = pNode
            self.listTail = pNode
        else:
            self.listTail.right = pNode
            pNode.left = self.listTail
            self.listTail = pNode
        self.Convert(pNode.right)
        return self.listHead