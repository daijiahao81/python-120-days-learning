# continue关键字用于本次循环，中断本次循环进入下一次循环
for i in range(1,6):
    print("语句1")
    continue
    print("语句2")
# continue只作用在当前循环内，不影响其他循环
for x in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        continue
        print("语句3")
    print("语句4")

print("---------------------")
# break关键字，遇到直接循环终止

for c in range(1,101):
    print("语句1")
    break
    print("语句2")
print("语句3")

print("---------------------")

for x in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        break
        print("语句3")
    print("语句4")