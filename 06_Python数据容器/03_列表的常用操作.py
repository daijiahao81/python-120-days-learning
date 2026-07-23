# 定义列表
name_list = ["itheima", "itcast", "python"]

# 查看列表和数据类型
print(name_list)
print(type(name_list))

# 获取列表长度
print(f"列表长度：{len(name_list)}")

# 正数下标
print(f"第一个元素：{name_list[0]}")

# 负数下标
print(f"最后一个元素：{name_list[-1]}")

# 修改元素
name_list[1] = "传智教育"
print(name_list)

# 指定位置插入
name_list.insert(0, "best")
print(name_list)

# 追加单个元素
name_list.append("黑马程序员")
print(name_list)

# 追加多个元素
name_list.extend(["Python", "Git"])
print(name_list)

# 查询元素下标
if "python" in name_list:
    index = name_list.index("python")
    print(f"python 的下标是：{index}")

# 统计元素数量
print(f"Python 出现次数：{name_list.count('Python')}")

# 删除并接收被删除元素
deleted_value = name_list.pop()
print(f"删除的元素：{deleted_value}")
print(f"删除后的列表：{name_list}")

# 遍历列表
for item in name_list:
    print(item)

