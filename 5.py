class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
	def __str__(self):
		s = ""
		while self:
			s += str(self.val)
			self = self.next
		return s

# 利用栈先进后出，遍历的时候将每个节点放入栈，遍历完整个链表
# 再从栈顶开始逐个输出节点。
def reverseLinkedList1(node):
	if not node or not node.next:
		return node
	stack = []
	dummy = n = ListNode(0)
	while node:
		stack.append(node.val)
		node = node.next
	while len(stack) > 0:
		n.next = ListNode(stack.pop())
		n = n.next
	return dummy.next


# 直接翻转，利用两个指针：pre cur
def reverseLinkedList2(node):
	if not node or not node.next:
		return node
	pre = None
	cur = node
	dummy = node
	while cur:
		dummy = cur
		tmp = cur.next
		cur.next = pre
		pre = cur
		cur = tmp
	return dummy



n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print(n1)

print(reverseLinkedList1(n1))
print(reverseLinkedList1(None))
print(reverseLinkedList1(n5))


print(reverseLinkedList2(n1))
