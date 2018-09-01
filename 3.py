# solution 1
# 从右上角出发，如果当前元素大于目标元素，则一定在左边区域(列-1)，
# 如果当前元素小于目标元素，则一定在下方区域(行+1)

# solution 2
# 从左下角出发，如果当前元素大于目标元素，则一定在上方区域(行-1)，
# 如果当前元素小于目标元素，则一定在右方区域(列+1)

# warning:
# 不能从左上角或者右下角找，因为会产生查找重叠。
# 比如从左上角查找，如果当前元素<目标元素，则可能在右边区域，
# 也可能在下方区域，所以会重叠。

def arrayFinder(array, target):
	row = len(array)
	col = len(array[0])
	# if target < array[0][0] or target > array[row-1][col-1]:
	# 	return False
	i = 0
	j = col - 1
	found = False
	while i >= 0 and i < row and j >= 0 and j < col and not found:
		if target == array[i][j]:
			found = True
		elif target < array[i][j]:
			j -= 1
		elif target > array[i][j]:
			i += 1
	return found

a1 = [1, 2, 8, 9]
a2 = [2, 4, 9, 12]
a3 = [4, 7, 10, 13]
a4 = [6, 8, 11, 15]
a = [a1, a2, a3, a4]
print(arrayFinder(a, 6))

