# 首先用quick sort排好数组，如果存在出现次数超过一半的数字，
# 它必在数组中间位置。直接取出中间位置的元素，遍历计算次数
# 如果超过数组长度一半，则为此数字，否则返回0
class Solution:
    # quick sort
    def quickSort(self, alist):
        self.quickSortHelper(alist, 0, len(alist) - 1)
    def quickSortHelper(self, alist, first, last):
        if first < last:
            splitspot = self.partition(alist, first, last)
            self.partition(alist, first, splitspot - 1)
            self.partition(alist, splitspot + 1, last)
    
    def partition(self, alist, first, last):
        pivotvalue = alist[first]
        finished = False
        left = first + 1
        right = last
        while not finished:
            while left <= right and alist[left] <= pivotvalue:
                left += 1
            while left <= right and alist[right] >= pivotvalue:
                right -= 1
            if left > right:
                finished = True
            else:
                alist[left], alist[right] = alist[right], alist[left]
        alist[first], alist[right] = alist[right], alist[first]
        return right 
    
    def findNum(self, alist):
        self.quickSort(alist)
        mid = len(alist) // 2
        count = 0
        for num in alist:
            if num == alist[mid]:
                count += 1
        return alist[mid] if count > len(alist) / 2 else 0

# test
test = Solution()
alist = [1, 2, 3, 2, 2, 2, 5, 4, 2]
print(test.findNum(alist))
alist = [1, 2, 3, 2, 2, 2, 5, 4, 2, 6, 7, 8, 9]
print(test.findNum(alist))