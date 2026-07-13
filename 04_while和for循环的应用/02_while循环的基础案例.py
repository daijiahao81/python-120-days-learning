import random
# 定义1-100的随机数
random_number = random.randint(1,100)
# 定义一个变量用来存储猜测次数
count = 0

flag = True
while flag:
    # 定义一个容器接受猜的数字
    guess_number = int(input("请输入你猜测的数字:"))
    count += 1
    if guess_number == random_number:
        print("恭喜你，猜对了！")
        flag = False
    else:
        if guess_number > random_number:
            print("您猜的大了")
        else:
            print("您猜的小了")
print(f"你总共猜测了{count}次")