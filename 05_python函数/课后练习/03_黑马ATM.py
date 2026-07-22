# 定义一个全局变量 money
money = 5000000

# 定义全局变量 name
name = None

# 要求客户输入姓名
name = input("请输入您的姓名:")


# 定义查询函数
def query(show_header):
    if show_header:
        print("----------查询余额----------")
    print(f"{name},您好,您的余额剩余:{money}元")

# 定义存款函数
def saving(num):
    global money
    money += num
    print("----------存款----------")
    print(f"{name},您好,您存款:{num}元成功")

    # 调用查询函数,通过参数控制输出内容
    query(False)

# 定义取款函数
def get_money(num):
    global money
    if num > money and money == 0:
        print(f"取款失败,您的余额不足,剩余{money}元")
    else:
        money -= num
        print("----------取款----------")
        print(f"{name},您好,您取款:{num}元成功")
    

    # 调用查询函数,通过参数控制输出内容
    query(False)

# 定义主菜单函数
def main():
    print("----------主菜单----------")
    print(f"{name},您好,欢迎来到黑马银行ATM,请选择操作:")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择:")

# 定义无限循环
while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num = int(input("请输入您要存入的金额:"))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("请输入您要取出的金额:"))
        # if num > money:
        #     print(f"取款失败,您的余额不足,剩余{money}元")
        get_money(num)
        continue
    else:
        print("程序退出")
        break