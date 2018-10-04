# 利用quick select，每次取最后一个数pivot，left存放<=pivot的数
# 如果len(left)等于k，则left就是最小的k个数
# 如果len(left)大于k，则递归从left中找最小的k个
# 如果len(left)小于k，则right存放>pivot的数，递归从right中取k-len(left)个数
def kMinNum(alist, k):
    if len(alist) < k:
        return alist
    pivot = alist[-1]
    left = [pivot] + [num for num in alist[:-1] if num <= pivot]
    if len(left) == k:
        return left
    if len(left) > k:
        return kMinNum(left, k)
    else:
        right = [num for num in alist[:-1] if num > pivot]
        return kMinNum(right, k - len(left)) + left

# test
for i in range(1, 6):
    print(kMinNum([11, 8, 4, 1, 5, 2, 7, 9], i))