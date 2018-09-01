# 暴力替换
# 从头到尾扫描字符，遇到空格就先将剩余字符整体
# 往后移动2个位置，然后替换为%20，但这样时间复杂度为O(n^2)

# O(n)解法：
# 先遍历字符串，计算出空格个数
# 然后在原字符串后面加上(空格数*2)的长度，就是新字符串的长度
# 从后往前遍历字符串，如果没有遇到空格，就在当前位置赋值为原来的字符
# 若遇到空格，则往前推两个位置，填充%20.

# warning！！！！！！！！！
# python中string是immutable，因此在执行函数的时候，首先转化为list
# 最后在"".join(list)返回字符串。

def replaceSpace(s, length): 
	# length: maximum length of the array
	if s == None or length <= 0:
		return 
	# count the number of blanks
	count = s.count(' ')
	s_length = len(s)

	# compute the replaced string length
	rep_length = s_length + count * 2
	if rep_length > length:
		return 
	# extend the string 
	s += ["" for i in range(rep_length - s_length)]

	# replace the blank with "%20"
	i = s_length - 1
	j = rep_length - 1
	while i != j:
		if s[i] == ' ':
			j -= 2
			s[j: j+3] = '%20'
		else:
			s[j] = s[i]
		i -= 1
		j -= 1
	return s



a = "we are young"

print(''.join(replaceSpace(list(a), 100)))