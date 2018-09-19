# 二叉排序树或者是一棵空树，或者是具有下列性质的二叉树：
# 若左子树不空，则左子树上所有结点的值均小于它的根结点的值；
# 若右子树不空，则右子树上所有结点的值均大于或等于它的根结点的值；
# 左、右子树也分别为二叉排序树；
# 没有键值相等的节点。
def verifySequenceOfBST(sequence):
    if len(sequence) == 0:
        return True
    return judge(sequence, 0, len(sequence) - 1)

def judge(sequence, left, right):
    if left >= right:
        return True
    # 根节点为最后一个元素
    root = sequence[right]
    mid = right - 1
    # 找出右子树范围
    while sequence[mid] > root:
        mid -= 1
    i = left
    # 找出左子树范围
    while i < mid and sequence[i] < root:
        i += 1
    if i < mid:
        return False
    # 左子树：[left : mid]
    # 右子树：[mid + 1 : right - 1]
    # 根：right
    return judge(sequence, left, mid) and judge(sequence, mid + 1, right - 1)

# test
testse = [2, 9, 5, 10, 17, 15, 19, 18, 12]
print(verifySequenceOfBST(testse))
testse2 =[7, 4, 6, 5]
print(verifySequenceOfBST(testse2))
    