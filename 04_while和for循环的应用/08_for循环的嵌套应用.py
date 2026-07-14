# 用for循环嵌套完成像小美表白100天，每天送10朵玫瑰花

i = 0
# 外层循环
for i in range(1,101):
    print(f"今天是第{i}天，准备表白")

    # 内层循环
    for x in range(1,11):
        print(f"给小美送的第{x}朵玫瑰花")
    
    print("小美我喜欢你")
print(f"第{i}天，表白成功")