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

# 双指针法
# 注意边界情况：
# 1. 空链表
# 2. 链表长度<k
def findKthNode(linkedlist, k):
	if linkedlist == None:
		print("NULL linkedlist!")
		return
	right = linkedlist
	left = linkedlist
	i = 0
	while right and i < k:
		right = right.next
		i += 1
	if right == None and i < k:
		print("The list length is less than K!")
		return
	while right != None:
		right = right.next
		left = left.next
	return left.val

# test
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

print(findKthNode(n1, 3))
print(findKthNode(n1, 6))


