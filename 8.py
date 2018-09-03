# 暴力搜索
def findMinNumInRotateArray1(array):
	if len(array) == 0:
		return None
	min_num = array[0]
	for i in range(1, len(array)):
		if array[i] < array[i - 1]:
			min_num = array[i]
	return min_num


# Binary Search
def findMinNumInRotateArray2(array):
	if len(array) == 0:
		return None
	left = 0
	right = len(array) - 1
	mid = 0
	if array[left] < array[right]:
		return array[0]
	while array[left] >= array[right]:
		if right - left == 1:
			mid = right
			break
		mid = (left + right) // 2
		# 如果中间的数既等于left又等于right，则顺序查找
		if array[mid] == array[left] and array[mid] == array[right]:
			return inorderSearch(array, left, right)
		if array[mid] >= array[left]:
			left = mid
		elif array[mid] < array[right]:
			right = mid

	return array[mid]

def inorderSearch(array, left, right):
	minNum = array[0]
	for i in range(right - left):
		if array[left + i] < minNum:
			minNum = array[left + i]
	return minNum


# test
print(findMinNumInRotateArray1([3, 4, 5, 1, 2]))
print(findMinNumInRotateArray2([3, 4, 5, 1, 2]))