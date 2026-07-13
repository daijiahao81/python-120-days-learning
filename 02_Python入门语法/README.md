# 第二章：Python 入门语法

## 本章学习内容

本章代码包含以下内容：

- 变量及变量值的修改
- `int`、`float`、`str` 数据类型
- 使用 `type()` 查看数据类型
- 使用 `int()`、`float()`、`str()` 转换数据类型
- 标识符和变量命名规则
- 算术运算符
- 复合赋值运算符
- `input()` 的初步使用

## 一、变量

变量用于在程序运行过程中保存数据：

```python
money = 50
money -= 10
print(money)
```

赋值符号 `=` 表示把右侧的数据保存到左侧变量中。

变量的值可以改变：

```python
money = 50
money = 40
```

## 二、常用数据类型

### 整数 `int`

```python
age = 23
```

### 浮点数 `float`

```python
height = 1.75
```

### 字符串 `str`

```python
name = "小明"
```

可以使用 `type()` 查看数据类型：

```python
print(type(name))
print(type(age))
print(type(height))
```

## 三、数据类型转换

```python
number_text = "100"
number = int(number_text)

price_text = "3.14"
price = float(price_text)

age = 23
age_text = str(age)
```

需要注意，并非所有字符串都能转换成数字：

```python
int("abc")  # 会产生 ValueError
```

## 四、标识符与变量命名

标识符可由以下字符组成：

- 英文字母
- 数字
- 下划线

必须遵守：

- 不能以数字开头
- 不能使用 Python 关键字
- Python 区分大小写
- 不推荐使用中文变量名
- 建议采用小写字母和下划线命名

推荐写法：

```python
student_name = "小明"
student_age = 23
student_height = 1.75
```

## 五、算术运算符

| 运算符 | 含义 | 示例 |
|---|---|---|
| `+` | 加法 | `1 + 2` |
| `-` | 减法 | `5 - 2` |
| `*` | 乘法 | `3 * 4` |
| `/` | 除法 | `10 / 2` |
| `//` | 整除 | `11 // 2` |
| `%` | 取余 | `11 % 2` |
| `**` | 幂运算 | `2 ** 3` |

运算具有优先级，必要时使用括号：

```python
result = (1 + 2) * 3
```

## 六、复合赋值运算符

```python
num += 1
num -= 1
num *= 2
num /= 2
num //= 2
num %= 2
num **= 2
```

注意，原代码中：

```python
num ** 2
```

只进行了计算，却没有把结果保存回 `num`。应写成：

```python
num **= 2
```

或者：

```python
num = num ** 2
```

## 七、`input()` 输入

`input()` 用来接收用户输入，并且返回值默认是字符串：

```python
name = input("请输入姓名：")
age = int(input("请输入年龄："))
```

## 本章易错点

- `=` 是赋值，`==` 才是比较
- `input()` 的结果默认为字符串
- `/` 的结果通常是浮点数
- 变量名不能以数字开头
- `num ** 2` 不会自动修改 `num`
- 运算符两侧建议保留空格，提高可读性

## 本章总结

本章建立了 Python 编程最基础的数据处理能力：使用变量保存数据、识别和转换数据类型、规范命名变量，并通过运算符完成基本计算。

## 复习检查

- [x] 会定义和修改变量
- [x] 能区分 `int`、`float` 和 `str`
- [x] 会使用 `type()`
- [x] 会进行基础类型转换
- [x] 了解变量命名规则
- [x] 会使用常见算术运算符
- [ ] 熟练处理 `input()` 返回的字符串
- [ ] 熟练掌握复合赋值运算符
