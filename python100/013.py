# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，
# 因为153=1的三次方＋5的三次方＋3的三次方。

l1 = []
for i in range(100, 1000):
    if int(str(i)[0]) ** 3 + int(str(i)[1]) ** 3 + int(str(i)[2]) ** 3 == i:
        l1.append(i)

print(l1)
