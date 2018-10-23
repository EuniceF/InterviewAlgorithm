# course 1: bubble sort, selection sort, insertion sort, merge sort & two exercises
class solution:
    # bubble sort
    def bubbleSort(self, arr):
        if arr is None or len(arr) < 2:
            return
        for end in range(len(arr) - 1, 0, -1):
            for i in range(end):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return arr
    
    # selection sort
    def selectionSort(self, arr):
        if arr is None or len(arr) < 2:
            return
        for start in range(len(arr) - 1):
            minindex = start
            for i in range(start + 1, len(arr)):
                if arr[i] < arr[minindex]:
                    minindex = i
            arr[minindex], arr[start] = arr[start], arr[minindex]
        return arr
    
    # insertion sort
    def insertionSort(self, arr):
        if arr is None or len(arr) < 2:
            return
        for i in range(1, len(arr)):
            j = i - 1
            while j >= 0 and arr[j + 1] < arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j -= 1
        return arr
    
    # merge sort
    def mergeSort(self, arr):
        if arr is None or len(arr) < 2:
            return
        self.sortProcess(arr, 0, len(arr) - 1)
        return arr
    
    def sortProcess(self, arr, left, right):
        if left == right:
            return
        mid = left + ((right - left) >> 1)
        self.sortProcess(arr, left, mid)
        self.sortProcess(arr, mid + 1, right)
        self.mergeProcess(arr, left, mid, right)
    
    def mergeProcess(self, arr, left, mid, right):
        tmp = [0] * (right - left + 1)
        p1 = left
        p2 = mid + 1
        i = 0
        while p1 <= mid and p2 <= right:
            if arr[p1] < arr[p2]:
                tmp[i] = arr[p1]
                i += 1
                p1 += 1
            else:
                tmp[i] = arr[p2]
                i += 1
                p2 += 1
        while p1 <= mid:
            tmp[i] = arr[p1]
            i += 1
            p1 += 1
        while p2 <= right:
            tmp[i] = arr[p2]
            i += 1
            p2 += 1
        for i in range(len(tmp)):
            arr[left + i] = tmp[i]
    
    # 小和问题
    def smallSum(self, arr):
        if arr is None or len(arr) < 2:
            return 0
        return self.mergeSum(arr, 0, len(arr) - 1)
    
    def mergeSum(self, arr, left, right):
        if left == right:
            return 0
        mid = left + ((right - left) >> 1)
        return self.mergeSum(arr, left, mid) + self.mergeSum(arr, mid + 1, right) + self.merge(arr, left, mid, right)
    
    def merge(self, arr, left, mid, right):
        result = 0
        tmp = [0] * (right - left + 1)
        p1 = left
        p2 = mid + 1
        i = 0
        while p1 <= mid and p2 <= right:
            if arr[p1] < arr[p2]:
                result += arr[p1] * (right - p2 + 1)
                tmp[i] = arr[p1]
                i += 1
                p1 += 1
            else:
                tmp[i] = arr[p2]
                i += 1
                p2 += 1
        while p1 <= mid:
            tmp[i] = arr[p1]
            i += 1
            p1 += 1
        while p2 <= right:
            tmp[i] = arr[p2]
            i += 1
            p2 += 1
        for j in range(len(tmp)):
            arr[left + j] = tmp[j]
        return result





test = solution()
testarr = [5, 1, 3, 9, 4, 2, 10, 7]
print(test.bubbleSort(testarr))
print(test.selectionSort(testarr))
print(test.insertionSort(testarr))
print(test.mergeSort(testarr))
print(test.smallSum([1, 3, 4, 2, 5]))



# 逆序对问题
# class Solution:
#     def InversePairs(self, data):
#         # write code here
#         if data is None or len(data) < 2:
#             return 0
#         return self.mergeSort(data, 0, len(data) - 1)
#     def mergeSort(self, data, left, right):
#         if left == right:
#             return 0
#         mid = left + ((right - left) >> 1)
#         return self.mergeSort(data, left, mid) + self.mergeSort(data, mid + 1, right) + self.merge(data, left, mid, right)
#     def merge(self, data, left, mid, right):
#         count = 0
#         tmp = [0] * (right - left + 1)
#         p1 = left
#         p2 = mid + 1
#         i = 0
#         while p1 <= mid and p2 <= right:
#             if data[p1] > data[p2]:
#                 count += (right - p2 + 1)
#                 tmp[i] = data[p1]
#                 i += 1
#                 p1 += 1
#             else:
#                 tmp[i] += data[p2]
#                 i += 1
#                 p2 += 1
#         while p1 <= mid:
#             tmp[i] = data[p1]
#             i += 1
#             p1 += 1
#         while p2 <= right:
#             tmp[i] = data[p2]
#             i += 1
#             p2 += 1
#         return count
# test = Solution()
# import sys
# line = sys.stdin.readline().strip()
# lines = line.split(",")
# data = []
# for num in lines:
#     data.append(int(num))
# print(data)
# print(test.InversePairs(data)) 
