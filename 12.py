# 使用字符串模拟加法

def sumEmulator(num):
	i = len(num) - 1
	lastNum = ''
	while True:
		if i == -1:
			return 1
		elif num[i] == '9':
			lastNum = '0' + lastNum
		else:
			lastNum = str(int(num[i]) + 1) + lastNum
			return num[:i] + lastNum

