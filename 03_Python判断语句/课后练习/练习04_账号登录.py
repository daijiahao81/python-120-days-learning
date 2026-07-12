# 定义变量
correct_username = "admin"
correct_password = "123456"

username = input("请输入用户名:")
password = input("请输入密码:")

# 用if语句进行判断
if username == correct_username:
    if password == correct_password:
        print("登录成功")
    else:
        print("密码错误")
else:
    print("用户名错误")