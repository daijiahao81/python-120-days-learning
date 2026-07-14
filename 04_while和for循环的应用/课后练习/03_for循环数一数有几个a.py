# 定义字符串变量
name = "itheima is a brand of itcast"
# 定义变量用来记录有几个a
count = 0
# for循环便利
# 通过if判断
for x in name:
    if x == "a":
        count += 1
print(f"itheima is a brand of itcast中共含有:{count}个字母a")