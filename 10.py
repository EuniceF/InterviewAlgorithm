# 补码：
# 正数的补码是其本身
# 负数的补码是在其原码的基础上，符号位不变，其余各位取反，然后+1

# built-in function
def NumberOfOne1(n):
	if n >= 0:
		return bin(n).count('1')
	else:
		return bin(n & 0xffffffff).count('1')


# 如果一个整数n!=0，则这个整数至少有一位是1.如果把这个整数-1，则
# 原来位于整数最右边的1的位置就会变为0，若最右边1的右边还有0，则这些0变为1
# 其余位置不变。例：1011 - 1 -> 1010   1100 - 1 -> 1011
# 所以 n&(n-1) 会将n最右边的1变为0，循环，直到所有位都变为0，循环次数
# 即为1的个数
def NumberOfOne2(n):
	count = 0
	while n != 0:
		count += 1
		n = n & (n - 1)
	return count


# !!!!waring:
# 以上解法如果n<0，则会出现无限循环的现象
# 在python3中，当长度超过32位或64位，python3会自动将其转为长整型，即没有长度限制
# 所以要确保n为正数
# 优化：
def NumberOfOne3(n):
	count = 0
	while n&0xffffffff != 0:
		count += 1
		n = n & (n - 1)
	return count


# test
print(NumberOfOne1(3))
print(NumberOfOne1(4))
print(NumberOfOne1(5))
print(NumberOfOne1(-1))

print(NumberOfOne3(3))
print(NumberOfOne3(4))
print(NumberOfOne3(5))
print(NumberOfOne3(-1))