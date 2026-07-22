# 定义函数,嵌套使用
def func_b():
    print("---2---")

def func_a():
    print("---1---")

    func_b()

    print("---3---")

# 调用函数func_a
func_a()