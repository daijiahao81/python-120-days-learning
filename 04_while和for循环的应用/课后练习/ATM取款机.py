# ATM自动存取款机

# 定义初始账户金额5000元
money = 5000



while True:
    print("======ATM======")
    print()
    print("1.查询余额")
    print("2.存款")
    print("3.取款")
    print("4.退出")
    # 定义功能查询、存款、取款、退出
    select = int(input("请选择您要办理的业务："))
    # 查询功能
    if select == 1:
        print(f"您的账户余额为：{money}")
    # 存入功能
    elif select == 2:
        deposit = int(input("请输入您要存入的金额："))
        money += deposit
        print(f"您的账户余额为：{money}")
    # 取出功能
    elif select == 3:
        withdrawal = int(input("请输入你要取出的金额："))
        money -= withdrawal
        print(f"您的账户余额为：{money}")
    # 退出break结束循环
    else:
        break