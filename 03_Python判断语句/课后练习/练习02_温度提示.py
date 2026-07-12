# 定义温度变量
temperature = float(input("请输入当前温度（摄氏度）:"))

# 用if语句进行判断
if temperature >= 35:
    print("高温天气，请注意防暑")
elif temperature >= 25:
    print("天气较热")
elif temperature >= 10:
    print("温度适宜")
else:
    print("天气较冷，请注意保暖")