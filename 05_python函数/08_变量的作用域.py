# 定义一个全局变量
num = 100 # 全局变量

def testA():
    # 利用global关键字声明全局变量
    global num 
    num = 200 #局部变量
    
    
    print(num)

testA()
print(num)