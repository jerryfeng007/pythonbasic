print('--------------------------------------去除空白单词---------------------------------------------------------')

con = ['a', 'b', 'c', '', 0, None, [], (), {}, set()]
con = list(filter(None, con))  # 可以过滤0、None、空字符串、空列表、空字典、空元组等，注意别过滤多了
print(con)  # ['a', 'b', 'c']
