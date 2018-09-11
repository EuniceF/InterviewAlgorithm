# 冒泡排序
def isOdd(n):
	return n % 2 != 0

def isEven(n):
	return n % 2 == 0

def reOrderArray1(array):
	exchange = True
	passnum = len(array) - 1
	while passnum >= 0 and exchange:
		exchange = False
		for i in range(passnum):
			if isEven(array[i]) and isOdd(array[i + 1]):
				exchange = True
				array[i], array[i + 1] = array[i + 1], array[i]
		passnum -= 1
	return array


# 辅助数组
def reOrderArray2(array):
	temp = []
	for num in array:
		if isEven(num):
			temp.append(num)
			array.remove(num)
	array.extend(temp)
	return array


# test
print(reOrderArray1([1, 2, 3, 4, 5, 6, 7]))
print(reOrderArray2([1, 2, 3, 4, 5, 6, 7]))

