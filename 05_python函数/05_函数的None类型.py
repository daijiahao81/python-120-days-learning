# 无return的语句函数返回值
def say_hi():
    print("你好呀")

result = say_hi()
print(f"无返回值函数, 返回的内容是: {result}")
print(f"无返回值函数, 返回的内容类型是: {type(result)}")
# 函数返回值返回None
def say_hi2():
    print("你好呀")
    return None
result2 = say_hi()
print(f"无返回值函数, 返回的内容是: {result2}")
print(f"无返回值函数, 返回的内容类型是: {type(result2)}")


# None用于if判断
def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None
    
result = check_age(16)
if not result:
    print("未成年, 不许进入")