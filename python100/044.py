# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
#
X = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
#
Y = [[5, 8, 1],
    [6, 7, 3],
    [4, 5, 9]]

z = [[X[0][0] + Y[0][0], X[0][1] + Y[0][1], X[0][2] + Y[0][2]],
     [X[1][0] + Y[1][0], X[1][1] + Y[1][1], X[1][2] + Y[1][2]],
     [X[2][0] + Y[2][0], X[2][1] + Y[2][1], X[2][2] + Y[2][2]]]

print(z)
