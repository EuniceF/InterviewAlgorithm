class Solution:
    # 将arr中比num小的数放在左边，比num大的数放在数组右边
    def leftSmallRightLarge(self, arr, num):
        if arr is None or len(arr) < 2:
            return arr
        curr = 0
        less = -1
        while curr < len(arr):
            if arr[curr] <= num:
                self.swap(arr, curr, less + 1)
                less += 1
            curr += 1
        return arr
    
    def swap(self, arr, index1, index2):
        arr[index1], arr[index2] = arr[index2], arr[index1]
    
    # 荷兰国旗问题 arr = [less, equal, more]
    def hollandFlag(self, arr, left, right, num):
        less = left - 1
        more = right + 1
        curr = left
        while curr < more:
            if arr[curr] < num:
                self.swap(arr, less + 1, curr)
                less += 1
                curr += 1
            elif arr[curr] > num:
                self.swap(arr, more - 1, curr)
                more -= 1
            else:
                curr += 1
        return arr

    # quick sort(优化)
    def quickSort(self, arr, left, right):
        if left < right:  #一定要写这个！！！！！
            p = self.partition(arr, left, right)
            self.quickSort(arr, left, p[0] - 1)
            self.quickSort(arr, p[1] + 1, right)
        return arr

    def partition(self, arr, left, right):
        less = left - 1
        more = right
        while left < more:
            if arr[left] < arr[right]:
                self.swap(arr, less + 1, left)
                left += 1
                less += 1
            elif arr[left] > arr[right]:
                self.swap(arr, more - 1, left)
                more -= 1
            else:
                left += 1
        self.swap(arr, more, right)
        return [less + 1, more]
    
    # 大根堆
    # i -> leftchild: 2*i+1; rightchild: 2*i+2; parent: (i-1)/2
    def heapSort(self, arr):
        if arr is None or len(arr) < 2:
            return arr
        heapsize = len(arr)
        for i in range(1, len(arr)):
            self.heapInsert(arr, i)
        self.swap(arr, 0, len(arr) - 1)
        heapsize -= 1
        while heapsize > 0:
            self.heapify(arr, 0, heapsize)
            heapsize -= 1
            self.swap(arr, 0, heapsize)
        return arr
    
    def heapInsert(self, arr, i):
        while arr[i] > arr[(i - 1) // 2] and i > 0:
            self.swap(arr, i, ((i - 1) // 2))
            i = (i - 1) // 2
    
    def heapify(self, arr, index, heapsize):
        left = index * 2 + 1
        while left < heapsize:
            if left + 1 < heapsize and arr[left] < arr[left + 1]:
                largest = left + 1
            else:
                largest = left
            largest = index if arr[index] > arr[largest] else largest
            if largest == index:
                break
            else:
                self.swap(arr, largest, index)
                index = largest
                left = index * 2 + 1
    




# test
test = Solution()
arr = [4, 6, 7, 3, 1, 8, 2, 9]
# arr2 = [4, 5, 6, 3, 1, 5, 8, 2, 5]
# print(test.leftSmallRightLarge(arr, 5))
# print(test.hollandFlag(arr2, 0, 8, 5))
# arr2 = [4, 5, 6, 3, 1, 5, 8, 2, 5]
# print(test.quickSort(arr2, 0, 8))
arr3 = [2, 1, 3, 6, 0, 4]
print(test.heapSort(arr))