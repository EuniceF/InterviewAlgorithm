# 思路：
# s1作为输入栈，s2作为输出栈

class Queue:
	def __init__(self):
		self.instack = []
		self.outstack = []

	def isEmpty(self):
		return len(self.instack) == 0 and len(self.outstack) == 0

	def enqueue(self, item):
		self.instack.append(item)
		print("Enter queue: ", item)

	def dequeue(self):
		if len(self.outstack) != 0:
			print("Out queue: ", self.outstack.pop())
		else:
			if self.isEmpty():
				print("Queue is empty!")
			else:
				while len(self.instack) != 0:
					self.outstack.append(self.instack.pop())
				print("Out queue: ", self.outstack.pop())

	def __len__(self):
		if len(self.outstack) == 0:
			return len(self.instack)
		else:
			return len(self.outstack)


# test
queue = Queue()
print(queue.isEmpty())
# enter queue
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.isEmpty())
print("Queue length: ", len(queue))

# out queue
queue.dequeue()
print("Queue length: ", len(queue))
queue.dequeue()
print("Queue length: ", len(queue))
queue.dequeue()
print("Queue length: ", len(queue))
queue.dequeue()
print("Queue length: ", len(queue))
queue.dequeue()
print(queue.isEmpty())