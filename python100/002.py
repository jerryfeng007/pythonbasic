# 题目：企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

ii = 120000


def li(i):
    j = 0
    a = i * 0.1
    b = 100000 * 0.1 + (i - 100000) * 0.075
    c = (i - 200000) * 0.05 + b
    d = (i - 400000) * 0.03 + c
    e = (i - 600000) * 0.015 + d
    f = (i - 1200000) * 0.01 + e

    if i <= 100000:
        j = a
    elif i > 100000:
        j = b
    elif i > 200000:
        j = c
    elif i > 400000:
        j = d
    elif i > 600000:
        j = e
    elif i > 1000000:
        j = f
    print(j)


li(ii)
