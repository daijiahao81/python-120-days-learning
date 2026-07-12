# 定义一个变量
num = 5
# 用if语句进行多轮判断
if int(input("请输入一个数字：")) == num:
    print("恭喜你，第一次就猜对了")
elif int(input("猜错了，再猜一次：")) == num:
    print("恭喜你猜对了")
elif int(input("猜错了，最后一次机会再猜一次：")) == num:
    print("恭喜你，最后一次机会猜对了")
else:
    print("很遗憾，你没有猜对")