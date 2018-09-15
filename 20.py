# 方法一
# 每次取出第一行添加到结果中，然后翻转矩阵
def printMatrix(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return matrix
    result = []
    while matrix:
        result += matrix.pop(0)
        if not matrix or not matrix[0]:
            break
        matrix = turn(matrix)
    return result


def turn(matrix):
    rowlen = len(matrix)
    collen = len(matrix[0])
    res = []
    for col in range(collen):
        temp = []
        for row in range(rowlen):
            temp.append(matrix[row][col])
        res.append(temp)
    res.reverse()
    return res



# 方法二
# 直接对列表遍历一次
def printMatrix2(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return matrix
    rowlen = len(matrix)
    collen = len(matrix)
    helpmatrix = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    isvisited = [[False for i in range(collen)] for j in range(rowlen)]
    result = []
    # 判断位置是否合法且未被访问过
    def judge(i, j):
        return i >= 0 and i < rowlen and j >= 0 and j < collen and not isvisited[i][j]
    i = 0
    j = 0
    d = 0
    count = rowlen * collen
    while count:
        result.append(matrix[i][j])
        isvisited[i][j] = True
        if not judge(i + helpmatrix[d][0], j + helpmatrix[d][1]):
            d += 1
            d %= 4  # 转弯
        i += helpmatrix[d][0]
        j += helpmatrix[d][1]
        count -= 1
    return result


# test
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
print(printMatrix(matrix))

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
print(printMatrix2(matrix))