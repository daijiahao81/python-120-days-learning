# 外层循环
for i in range(1,10):
    # 内层循环
    for x in range(1,i+1):
        print(f"{x} * {i} = {x*i}\t",end="")
    print()