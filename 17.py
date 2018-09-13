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

def mergeTwoSortedList(list1, list2):
    if list1 == None and list2 != None:
        return list2
    if list2 == None and list1 != None:
        return list1
    if list1 == None and list2 == None:
        return None
    # 生成头节点
    newlist = ListNode(0)
    head1 = list1
    head2 = list2
    if head1.val < head2.val:
        newlist.next = head1
        head1 = head1.next
    else:
        newlist.next = head2
        head2 = head2.next
    # 遍历两个链表
    curr = newlist.next
    while head1 and head2:
        if head1.val < head2.val:
            curr.next = head1
            curr = curr.next
            head1 = head1.next
        else:
            curr.next = head2
            curr = curr.next 
            head2 = head2.next
    # 处理剩余的链表
    if head1 != None:
        curr.next = head1
    if head2 != None:
        curr.next = head2
    return newlist.next

# test
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(8)
n5 = ListNode(10)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(7)
p4 = ListNode(8)
p5 = ListNode(9)
p6 = ListNode(10)
p7 = ListNode(12)
p1.next = p2
p2.next = p3
p3.next = p4
p4.next = p5
p5.next = p6
p6.next = p7

print(mergeTwoSortedList(n1, p1))
        