# # 定义变量
# first_number = int(input("请输入第一个数字:"))
# operator = input("请输入运算符(+、-、*、/):")
# second_number = int(input("请输入第二个数字:"))


# # 用if语句进行判断计算
# if operator == "+":
#     print(first_number + second_number)
# elif operator == "-":
#     print(first_number - second_number)
# elif operator == "*":
#     print(first_number * second_number)
# else:
#     print(first_number / second_number)    

# 修改后代码
# 定义变量
first_number = float(input("请输入第一个数字:"))
operator = input("请输入运算符(+、-、*、/):")
second_number = float(input("请输入第二个数字:"))


# 用if语句进行判断计算
if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "/":
    if second_number == 0:
        print("除数不能为零")
    else:
        print(first_number / second_number)
else:
    print("暂不支持该运算")