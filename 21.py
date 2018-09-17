# 利用两个栈
# stack存放数据
# minstack存放最小值
class Stack:
    def __init__(self):
        self.stack = []
        self.minstack = []
    
    # push
    def pushitem(self, item):
        self.stack.append(item)
        if len(self.minstack) == 0 or item < self.minstack[0]:
            self.minstack.append(item)
        else:
            # 将最小值再次入栈
            self.minstack.append(self.minstack[-1])
        
    # pop
    def popitem(self):
        if len(self.stack) != 0 and len(self.minstack) != 0:
            self.stack.pop()
            self.minstack.pop()
        else:
            return

    # find the min element in stack
    def minitem(self):
        if self.minstack:
            return self.minstack[-1]
        return None
    
    def __str__(self):
        return str(self.stack)

        


# test
st = Stack()
st.pushitem(2)
print(st)
print(st.minitem())

st.pushitem(3)
print(st)
print(st.minitem())

st.pushitem(1)
print(st)
print(st.minitem())

st.popitem()
print(st)
print(st.minitem())

st.popitem()
print(st)
print(st.minitem())


    