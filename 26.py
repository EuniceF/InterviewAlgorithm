class RandomListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None


def clone(phead):
    cloneNext(phead);
    cloneRandom(phead)
    return connectNodes(phead)

# 复制next指针
def cloneNext(phead):
    pnode = phead
    while pnode:
        pclone = RandomListNode(pnode.val)
        pclone.next = pnode.next
        pnode.next = pclone
        pnode = pclone.next

# 复制random指针
def cloneRandom(phead):
    pnode = phead
    while pnode:
        pclone = pnode.next
        if pnode.random:
            pclone.random = pnode.random.next
        pnode = pclone.next

# 拆分，原始链表（奇数点），复制链表（偶数点）
def connectNodes(phead):
    pnode = phead
    pclonehead = None
    pclonenode = None
    if pnode:
        pclonehead = pclonenode = pnode.next
        pnode.next = pclonenode.next
        pnode = pnode.next
    while pnode:
        pclonenode.next, pclonenode = pnode.next, pclonenode.next
        pnode.next, pnode = pclonenode.next, pnode.next
    return pclonehead