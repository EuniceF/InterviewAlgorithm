# recursice -> stack overflow 时间复杂度呈指数增长!!!
def fibonacci(n):
	if n < 2:
		return n
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)


# 递归展开 -> O(n)
def fibonacci(n):
	if n < 2:
		return n
	first = 0
	second = 1
	res = 0
	for i in range(2, n + 1):
		res = first + second
		first = second
		second = res
	return res


# # test
# for i in range(9):
# 	print(fibonacci(i))



# **********************************************************
# 扩展1：跳台阶
# **********************************************************
# 分为两种情况（这两种情况需要相加）：
# 1. 先跳1级，后面需要跳N-1级
# 2. 先跳2级，后面需要跳N-2级
# 由此可以推出：
# N = 0, solutions = 0
# N = 1, solutions = 1
# N = 2, solutions = 2
# => solutions = f(N - 1) + f(N - 2)

def jump(n):
	if n < 3:
		return n
	first = 1
	second = 2
	res = 0
	for i in range(3, n + 1):
		res = first + second
		first = second
		second = res
	return res



# **********************************************************
# 扩展2：矩形覆盖
# **********************************************************
# 2*n的矩形方法数 -> f(n)
# 第一个2*1的小矩形覆盖大矩形的左边，有两种放法：
# 1. 竖着放，还剩f(n - 1)种放法（放一个即可）
# 2. 横着放，还剩f(n - 2)种放法（放两个）
# => f(n) = f(n - 1) + f(n - 2)

def rectCover(n):
	if n < 2:
		return n
	first = 0
	second = 1
	res = 0
	for i in range(2, n + 1):
		res = first + second
		first = second
		second = res
	return res



