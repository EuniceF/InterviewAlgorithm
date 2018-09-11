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


# 三指针滑动
# pre -> cur -> next
def reverseLinkedList(linkedlist):
	if linkedlist == None or linkedlist.next == None:
		return linkedlist
	pre = None
	cur = linkedlist
	dummy = linkedlist
	while cur:
		dummy = cur
		next = cur.next
		cur.next = pre
		pre = cur
		cur = next
	return dummy


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

print(reverseLinkedList(n1))

