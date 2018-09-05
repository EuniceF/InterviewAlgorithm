# 常规方法(处理边界！！！！！！！！！！！！！)
# 1. 指数e=0，return 1
# 2. 指数e<0，return 1/(base^(-e))
# 3. 指数为负数时，底数 base!=0
# 注意base为float类型
def power(base, e):
	if e == 0:
		return 1.0
	isminus = False
	if e < 0:
		isminus = True
		e = e * (-1)
	res = 1
	for i in range(e):
		res = res * base
	if isminus:
		if base == 0.0:
			print("Error! Base can't be 0 when exponent is less than 0")
			return 
		else:
			res = 1.0 / res
	return res

# test
print(power(0.0, 0))
print(power(5.0, 0))
print(power(2.0, 3))
print(power(2.0, -3))
print(power(-2.0, 3))
print(power(0.0, -3))


# 二进制法(高效！！！！！！！！！！！！)
# e可以表示为两种情况：
# 1. e为奇数：base^e = base^(e/2) * base^(e/2)
# 2. e为偶数：base^e = base * base^((e-1)/2) * base^((e-1)/2)
# 二进制法判断奇偶： e & 1 == 1 ? 奇数 : 偶数
# 二进制法代替除以2： e >> 1
def bitPower(base, e):
	if e == 0:
		return 1.0
	if e == 1:
		return base
	isminus = False
	if e < 0:
		isminus = True
		e = e * (-1)
	if base == 0.0:
		if isminus:
			print("Error! Base can't be 0 when exponent is less than 0")
			return 
		else:
			return 0.0
	res = 1.0
	temp = base
	while e != 0:
		if e & 1 == 1: #当前指数为奇数
			res *= temp
		temp *= temp
		e >>= 1
	if isminus:
		res = 1.0 / res
	return res


# 递归写法
def recursiveBitPower(base, e):
	if e == 0:
		return 1.0
	if e == 1:
		return base

	isminus = False
	if e < 0:
		isminus = True
		e = e * (-1)
	if base == 0.0:
		if isminus:
			print("Error! Base can't be 0 when exponent is less than 0")
			return 
		else:
			return 0.0

	res = recursiveBitPower(base, e >> 1)
	res *= res
	if e & 1 == 1:
		res *= base

	if isminus:
		res = 1.0 / res

	return res


# test
print(bitPower(0.0, 0))
print(bitPower(5.0, 0))
print(bitPower(2.0, 3))
print(bitPower(2.0, -3))
print(bitPower(-2.0, 3))
print(bitPower(0.0, -3))


print(recursiveBitPower(0.0, 0))
print(recursiveBitPower(5.0, 0))
print(recursiveBitPower(2.0, 3))
print(recursiveBitPower(2.0, -3))
print(recursiveBitPower(-2.0, 3))
print(recursiveBitPower(0.0, -3))