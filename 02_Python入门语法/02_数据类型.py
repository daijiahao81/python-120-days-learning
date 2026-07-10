# 掌握使用type()语句查看数据类型
# string 字符串数据类型
# int 整数数据类型
# float 浮点数数据类型
# 直接打印三中变量数据类型
print(type("Hello World"))  # <class 'str'>
print(type(100))  # <class 'int'>
print(type(3.14))  # <class 'float'>

# 使用变量存储数据类型，type()语句查看变量数据类型
str_type = type("Hello World")
int_type = type(100)
float_type = type(3.14)
print(str_type)  # <class 'str'>
print(int_type)  # <class 'int'>
print(float_type)  # <class 'float'>

#使用type()语句查看变量存储的数据类型
name = "小明"
age = 23
height = 1.75
print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(height))  # <class 'float'>