# 通过index方法取到元素的下标值
mylist = ['itheima','itcast','python']
mylist2 = [1,2,3]
index = mylist.index('itheima')
print(f"itheima的元素下标是{index}")

# 修改特定下标索引的值
mylist[1] = "传智教育"
print(mylist)

# 在指定下标位置插入元素
mylist.insert(0,"best")
print(mylist)

# 列表中追加元素
mylist.append("黑马程序员")
print(mylist)

# 将其他的数据容器追加到指定列表尾部
mylist.extend(mylist2)
print(mylist)

# 删除列表元素
del mylist[4] # 通过del+列表下标删除
print(mylist)

mylist2.pop(2) # 通过列表方法pop删除
print(mylist2)
print(mylist)

mylist3 = [1,1,2,2,3,3,4,4,5,5,6,6]

# 删除某一个元素在列表中的第一个匹配项
mylist3.remove(1)
print(mylist3)

# 清空列表内容
mylist3.clear()
print(mylist3)

# 统计某元素在列表中的数量
mylist3 = [1,1,2,2,3,3,4,4,5,5,6,6]
count = mylist3.count(5)
print(count)