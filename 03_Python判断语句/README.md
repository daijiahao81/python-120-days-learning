# 第三章：Python 判断语句

## 本章学习内容

- 布尔类型 `True` 和 `False`
- 比较运算符
- `if` 单分支判断
- `if...else` 双分支判断
- `if...elif...else` 多分支判断
- 嵌套判断
- 逻辑运算符
- 判断语句综合练习

## 一、布尔类型

布尔类型只有两个值：

```python
True
False
```

比较表达式的结果也是布尔值：

```python
print(10 > 5)   # True
print(10 == 20) # False
```

## 二、比较运算符

| 运算符 | 含义 |
|---|---|
| `==` | 等于 |
| `!=` | 不等于 |
| `>` | 大于 |
| `<` | 小于 |
| `>=` | 大于等于 |
| `<=` | 小于等于 |

## 三、`if` 判断

```python
age = int(input("请输入年龄："))

if age >= 18:
    print("你已经成年了")
```

Python 使用缩进表示代码所属层级，通常使用 4 个空格。

## 四、`if...else`

```python
if age >= 18:
    print("你已经成年了")
else:
    print("你还未成年")
```

条件为真时执行 `if`，否则执行 `else`。

## 五、`if...elif...else`

适合多个互斥条件：

```python
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

判断从上到下执行，命中一个分支后，其余分支不会继续执行。因此范围判断通常应从严格或较大的条件开始。

## 六、逻辑运算符

### `and`

所有条件都成立时结果为真：

```python
if username == "admin" and password == "123456":
    print("登录成功")
```

### `or`

任意一个条件成立时结果为真：

```python
if score < 0 or score > 100:
    print("成绩输入错误")
```

### `not`

对条件结果取反：

```python
if not is_logged_in:
    print("请先登录")
```

## 七、嵌套判断

你的账号登录练习使用了嵌套判断：

```python
if username == correct_username:
    if password == correct_password:
        print("登录成功")
    else:
        print("密码错误")
else:
    print("用户名错误")
```

嵌套判断适合第二个条件依赖第一个条件的情况，但层级过多时会降低可读性。

## 八、已完成练习

### 奇偶数判断

核心思路：

```python
if number % 2 == 0:
    print("偶数")
else:
    print("奇数")
```

### 温度提示

通过从高到低排列温度条件，实现区间分类。

### 成绩等级

先检查输入范围，再按成绩从高到低判断等级。

### 账号登录

分别判断用户名和密码，练习嵌套 `if`。

### 简易计算器

根据运算符选择对应计算逻辑。

## 代码改进建议

简易计算器不应把所有未知运算符都当作除法，应明确判断 `/`：

```python
if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "/":
    if second_number == 0:
        print("除数不能为0")
    else:
        print(first_number / second_number)
else:
    print("不支持该运算符")
```

## 本章易错点

- 把赋值 `=` 写成比较 `==`，或反过来
- 忘记在 `if`、`elif`、`else` 后写冒号
- 缩进不一致
- 多分支条件顺序错误
- 没有处理非法输入
- 除法没有判断除数是否为 0
- 嵌套层级过深

## 本章总结

本章已经能够让程序根据不同条件选择不同执行路径，并完成了奇偶数、温度、成绩、登录和计算器等实际案例。这是编写交互式程序的重要基础。

## 复习检查

- [x] 理解布尔值
- [x] 会使用比较运算符
- [x] 会编写双分支和多分支判断
- [x] 会使用 `and` 和 `or`
- [x] 会编写嵌套判断
- [ ] 熟练处理非法输入
- [ ] 熟练设计无遗漏的条件分支
