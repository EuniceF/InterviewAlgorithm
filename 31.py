# dp方法
# fmax(x) = alist[i]            if i=0 or f(i-1)<=0
# fmax(x) = alist[i] + f(i-1)   if i!=0 and f(i-1)>0
def maxSum(alist):
    max_sum = alist[0]
    pre_sum = 0
    for num in alist:
        if pre_sum <= 0:
            pre_sum = num
        else:
            pre_sum = num + pre_sum
        if pre_sum > max_sum:
            max_sum = pre_sum
    return max_sum

# test
print(maxSum([6,-3,1,-2,7,-15,1,2,2]))