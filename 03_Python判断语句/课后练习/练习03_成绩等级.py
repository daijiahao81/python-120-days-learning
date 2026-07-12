# 定义成绩变量
score = int(input("请输入你的成绩(1-100):"))

# 用if语句进行判断
if score >100 or score < 0:
    print("成绩输入错误，请重新输入")
elif score >= 90:
    print("成绩优秀")
elif score >= 80:
    print("成绩良好")
elif score >= 60:
    print("成绩及格")
else:
    print("成绩不及格")