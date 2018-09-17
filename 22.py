def pushPopStack(list1, list2):
    if len(list1) != len(list2):
        return False
    if len(list1) == 0 and len(list2) == 0:
        return True
    # 根据list1和list2模拟出入栈
    stack = []
    # 设置两个指针指向list1和list2
    pl1 = 0
    pl2 = 0
    while True:
        item = list1[pl1]
        stack.append(item)
        # 若栈顶元素为出栈元素，则出栈，并查看下一个出栈元素
        while stack and stack[-1] == list2[pl2]:
            stack.pop()
            pl2 += 1
        # 若入栈指针移到最后，所有元素也应该全部出栈，此时栈应该为空
        if pl1 == len(list1) - 1:
            return len(stack) == 0
        # 查看下一个入栈元素
        pl1 += 1

# test
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 3, 2, 1]
print(pushPopStack(list1, list2))

list3 = [4, 3, 5, 1, 2]
print(pushPopStack(list1, list3))
