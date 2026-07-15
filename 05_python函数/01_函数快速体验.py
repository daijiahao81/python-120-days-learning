# 定义三个字符串
str1 = "itheima"
str2 = "itcast"
str3 = "python"

# 定义一个计数的变量
count = 0
# 用for循环便利str1字符床，利用count统计出字符串长度
for i in str1:
    count += 1
print(f"字符串{str1}的长度是：{count}")

# 函数，将上面的for循环封装成函数
def my_len(date):
    count = 0
    for i in date:
        count += 1
    print(f"字符串{str1}的长度是：{count}")


my_len(str1)
my_len(str2)
my_len(str3)