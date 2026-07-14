# 第四章：while 和 for 循环的应用——while 部分

## 本章学习内容

目前已完成 `while` 循环部分，包括：

- `while` 基础语法
- 固定次数循环
- 累加计算
- 布尔变量控制循环
- 猜数字案例
- `while` 嵌套
- `print()` 的 `end` 参数
- 制表符 `\t`
- 九九乘法表

## 一、`while` 基础结构

```python
循环变量 = 初始值

while 循环条件:
    循环体
    修改循环变量
```

示例：

```python
i = 0

while i < 100:
    print("执行循环")
    i += 1
```

`while` 会在条件为 `True` 时持续执行。

## 二、避免死循环

`while` 不会自动修改循环变量，因此必须确保条件最终能够变成 `False`：

```python
i = 1

while i <= 10:
    print(i)
    i += 1
```

如果遗漏 `i += 1`，程序可能无限运行。

## 三、累加器

求 1 到 100 的和：

```python
i = 1
sum_number = 0

while i <= 100:
    sum_number += i
    i += 1

print(sum_number)
```

其中：

- `i` 是循环变量
- `sum_number` 是累加器

最终结果为 `5050`。

## 四、布尔变量控制循环

猜数字案例使用了布尔标记：

```python
flag = True

while flag:
    guess_number = int(input("请输入你猜测的数字："))

    if guess_number == random_number:
        flag = False
```

当猜对后，把 `flag` 修改为 `False`，循环结束。

更常见的另一种写法是：

```python
while True:
    if 猜对条件:
        break
```

## 五、循环次数统计

```python
count = 0

while 条件:
    count += 1
```

可以统计用户猜测次数、任务执行次数或数据处理数量。

## 六、嵌套循环

```python
i = 1

while i <= 3:
    j = 1

    while j <= 2:
        print(i, j)
        j += 1

    i += 1
```

外层每执行一次，内层通常完整执行一轮。

内层变量 `j` 应在外层循环内部重新初始化，否则第二轮外层循环时，内层循环可能无法再次执行。

## 七、九九乘法表

```python
i = 1

while i <= 9:
    j = 1

    while j <= i:
        print(f"{j} * {i} = {j * i}\t", end="")
        j += 1

    print()
    i += 1
```

- 外层循环控制行数
- 内层循环控制每行算式数量
- `j <= i` 形成三角形结构
- `end=""` 阻止自动换行
- `\t` 用于对齐内容
- `print()` 在每行结束后换行

## 八、当前代码改进建议

### 1. 玫瑰花案例的语义

当前内层循环执行 10 次，但每次输出“送10朵玫瑰花”，文字上会表示每天送了 100 朵。

可改为：

```python
j = 1

while j <= 10:
    print(f"送出第{j}朵玫瑰花")
    j += 1
```

### 2. 猜数字输入校验

当前直接执行：

```python
guess_number = int(input("请输入你猜测的数字："))
```

输入非数字时会产生 `ValueError`。学习异常处理后可使用 `try...except` 改进。

## 九、需要补充的循环控制语句

### `break`

立即退出当前循环：

```python
while True:
    command = input("输入 q 退出：")

    if command == "q":
        break
```

### `continue`

跳过本轮剩余代码，进入下一轮：

```python
i = 0

while i < 10:
    i += 1

    if i % 2 == 0:
        continue

    print(i)
```

使用 `continue` 时要特别注意循环变量更新的位置，避免死循环。

## 本章易错点

- 忘记更新循环变量
- 边界条件写错，例如 `<` 和 `<=`
- 嵌套循环中没有重置内层变量
- `continue` 导致更新语句无法执行
- 无限循环没有退出条件
- 循环输出次数与文字描述不一致

## 本章总结

目前已经掌握 `while` 的基础循环、累加器、状态控制、嵌套循环以及九九乘法表。下一阶段应继续学习 `for` 循环，并比较两种循环的适用场景。

## 复习检查

- [x] 会编写基础 `while` 循环
- [x] 会控制固定循环次数
- [x] 会使用累加器
- [x] 会使用布尔变量结束循环
- [x] 会编写嵌套循环
- [x] 会输出九九乘法表
- [ ] 熟练掌握 `break`
- [ ] 熟练掌握 `continue`
- [ ] 能独立排查死循环
- [ ] 完成 `for` 循环部分
## for 循环部分
## 一、基础语法
- 写法固定
- for 临时变量 in 待处理的数据集（序列）
循环满足条件时执行的代码
- for循环无法定义循环条件，只能被动处理数据
## 二、range语句
1、range(num) 获得一个从0开始到num结束的数字序列,不包含num
2、range（num1,num2）获得一个从num1开始到num2结束的数字序列,不包含num2
2、range（num1,num2，step）获得一个从num1开始到num2结束的数字序列,不包含num2
## 三、for循环的嵌套应用
for循环可以进行嵌套，也可以和while循环组合嵌套使用
## 注意空格缩进
## 四、continue和break