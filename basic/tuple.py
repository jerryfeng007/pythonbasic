
print('----------------------------------------------元组的定义-------------------------------------------------')

# 方式1
tuple1 = (1, 2, 3, 4, 5)  # 相比方式2，效率更高

# 方式2
# 把字符串转化为元组
tuple2 = tuple('abcde')
print(tuple2)


print('-----------------------------------------------元组的特性-------------------------------------------------')

# 不加括号，默认是元组
a = 1, 2
print(type(a))

# 如果元组只有一个元素，也需要加逗号
b = 1      # int
c = 1,     # tuple
d = (1,)   # tuple
print(type(b), type(c), type(d))

print('-----------------------------------------------元组转化为字符串-------------------------------------------')

# 把元组转化为字符串，跟列表转化为字符串一样，也是用''.join()函数
tuple3 = ('a', 'b', 'c')
s = ''.join(tuple3)
print(s)

print('-----------------------------------------------元组的拼接-------------------------------------------')

tuple4 = (1, 2, 3, 4)
tuple5 = (5, 6, 7)
tuple6 = tuple4 + tuple5
print(tuple6)

print('-----------------------------------------------元组的索引-------------------------------------------')

# 列表的索引，和字符串的索引不完全一样，因为可以通过索引来修改列表
# 元组的索引，和字符串的索引完全一样，因为字符串和元组都是不可修改的
tuple7 = tuple('hello')
print(tuple7[0])
print(tuple7[-1])
print(tuple7[:])
print(tuple7[::])
print(tuple7[::2])
print(tuple7[::-1])  # 反转
print(tuple7[4:1:-1])
print(tuple7[-1:-4:-1])
print(tuple7[4:1:1])

print('-----------------------------------------------元组的排序-------------------------------------------')

# sorted()
tuple9 = (3, 1, 0, -4, 6)
print(sorted(tuple9))  # 排序后是个列表，并且不会改变原来的元组
print(tuple9)

# reversed()
tuple10 = (1, 3, 0)
print(list(reversed(tuple10)))  # [0, 3, 1]

print('-----------------------------------------------元组的方法-------------------------------------------')

# max min sum
tuple8 = (1, 2, 3)
print(max(tuple8))
print(min(tuple8))
print(sum(tuple8))

# count
tuple10 = ('a', 'b', 'c', 'a', 'e')
print(tuple10.count('a'))

# index
print(tuple10.index('a'))  # 返回第一个匹配的索引，如果不存在则报错

'''
备注：
字符串有index和find方法，列表和元组只有index
index如果找不到会报错，find找不到返回-1
'''

print('----------------------------------------------如何理解元组的不可变-------------------------------------------------')

# 场景1
t1 = (1, 2, 3)
print(id(t1))
# 如果想改变t1，比如变成(1, 2, 3, 4)
# 那么就要重新开辟一块内存，id肯定就变了
t1 = (1, 2, 3, 4)
print(id(t1))  # id变了

# 场景2
t1 = (1, 2, 3)
t2 = t1
print(id(t1), id(t2))  # id是一样的

# 场景3
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(id(t1), id(t2))  # id是一样的

print('----------------------------------------------元组嵌套列表-------------------------------------------------')

# 仍可对列表进行操作
l9 = (1, 2, [3, 4], 5)
print(id(l9))

l9[2].append(5)
print(l9)
print(id(l9))       # 操作元组内的列表元素，操作之后，id仍然没有变

print('-------------------------------------------转化为元组--------------------------------------------------')
tuple()
