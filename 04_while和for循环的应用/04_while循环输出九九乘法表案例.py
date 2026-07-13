# 补充，print()输出不换行
print("hello ",end="")
print("world")
# 补充，制表符\t，可以让多行字符串对齐
print("hello\tworld")
print("itheima\tbest")


# 通过while循环输出九九乘法表
# 外层定义每一行的循环，共9行
i = 1
while i <= 9:
    # 内层定义每一行有几个内容，j=1
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j*i}\t",end="")
        j += 1
    i += 1
    print("")