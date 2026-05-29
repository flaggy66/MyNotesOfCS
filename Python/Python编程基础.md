# Python编程基础

Python官方文档：[Documentation](https://docs.python.org/3/)

## Python下载与安装

***通常Linux发行版和MacOS都预装有Python，只是Python的版本可能较低。***

### 直接下载Python解释器安装

Python官网地址：[Welcome to Python.org](https://www.python.org/)，根据操作系统以及要安装的版本和安装方式（通过安装程序安装或者解压软件包）进行下载与安装。

安装完成后需要检查操作系统的环境变量是否配置——**将Python的安装目录添加到系统环境变量中**。

在操作系统终端中输入`python --version`或`python -V`（大写字母`V`）检查Python是否安装成功。

**此种方式适用于：初始学习Python编程，对Python版本没有严格要求，不需要在不同的Python版本之间切换，项目使用的Python版本比较固定。**

**安装后的环境中只有一些基本的Python库和Python解释器，后续开发需要的库或包通过`pip`命令进行安装，不同项目间使用的库或包可能会冲突**。



### 使用Anaconda或Miniconda安装Python

***Anaconda和Miniconda都可以看作是Python的”发行版“——内置了Python，并且提供对Python包或库的管理工具`conda`，还能管理不同的虚拟Python环境，也即是可以创建和切换不同的Python版本，不同Python版本的环境（包、库）不会冲突，是隔开的***。

**Anaconda 包含 Python + conda(管理工具) + 1500 多个预装的科学包+ Anaconda Navigator(图形界面)。下好了就能直接干活，做数据分析常用的库都有，不需要自己一个个装。有图形界面，不想敲命令行的可以用鼠标点点点来管理环境。安装包就有几百兆，装完占用几个 G 的硬盘空间。**

**Miniconda只有 Python + conda(管理工具) + 极少数必须的基础包。下载快，安装快，几乎不占多余空间。想要什么库（比如 Pandas），必须自己输入`conda`命令去安装。**

#### 安装Anaconda或Miniconda

Anaconda官网地址：[Advance AI with Open Source | Anaconda](https://www.anaconda.com/)

Miniconda官网地址：[Miniconda - Anaconda](https://www.anaconda.com/docs/getting-started/miniconda/main)

| **特性**           | **Anaconda**             | **Miniconda**            |
| ------------------ | ------------------------ | ------------------------ |
| **安装包大小**     | 大 (~600MB+，解压后几GB) | 小 (~70MB，解压后几百MB) |
| **预装库数量**     | 1500+ (啥都有)           | 仅包含基础依赖           |
| **图形界面 (GUI)** | 有 (Anaconda Navigator)  | 无 (纯命令行)            |
| **上手难度**       | 低 (小白最爱)            | 中 (需要记几个命令)      |
| **灵活性**         | 低 (预装太多)            | 高 (按需安装)            |

**Miniconda是Anaconda的一个精简版，所以在下载地址里可以看到Miniconda使用的是Anaconda的域名**。

在官网下载之后，在运行安装程序时需要注意以下事项：

+ 选择安装的范围：为当前用户，或者为所有用户（需要管理员权限）。建议如果是个人电脑无所谓，如果是多用户使用的电脑就选择当前用户。
+ 选择安装路径时建议不要有中文或空格。
+ 将`Anaconda`或`Miniconda`**添加到系统环境变量中** （官方建议不勾选——因为可能会影响系统中其他的 Python。实际建议——勾选它会方便很多，直接在终端命令行中，如`cmd`里就能用 `conda` 命令。如果不勾，则必须通过专门的 "Anaconda Prompt" 快捷方式来操作或者自己配置环境变量）。
+ 根据情况勾选`Register as my default Python`选项，勾选——会让其他编辑器（如 VS Code）自动找到它。

安装完成后，在终端命令行（如`cmd`）或者`Anaconda Prompt`命令行（`Miniconda`也是这个）中输入`conda --version`，如果返回了版本号（例如 `conda 23.x.x`），说明安装成功。

对于国内使用来说还有一个很重的步骤就是**配置`conda`的国内镜像源**提高`conda`下载库或包的速度。

这里以配置`清华源`镜像源为例：

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/
conda config --set show_channel_urls yes
```

实际的配置过程可以上网搜索获得。

清华大学开源软件镜像站地址：[清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirrors.tuna.tsinghua.edu.cn/)



#### 安装Python（创建环境）

使用`conda`创建指定版本的Python环境的命令格式：`conda create -n [环境名称] python=[版本号]`。

例如，打开终端（Mac/Linux）或 `Anaconda Prompt`（Windows），输入以下命令：

```bash
conda create -n py38 python=3.8
```

+ `create`: 创建环境指令。

+ `-n py38`: 给这个环境起个名字，这里它是 `py38`。

+ `python=3.8`: 指定想要的 Python 版本。Conda 会自动去下载这个版本及其依赖。

**进阶技巧：** 如果你想在创建环境时顺便把常用的库装好，可以这样写：

```bash
# 创建一个 Python 3.9 环境，并预装 numpy 和 pandas
conda create -n data_env python=3.9 numpy pandas
```



#### 切换 Python 版本 (激活/退出环境)

创建好环境后，系统里就有多个 Python 环境。通过“激活”命令来告诉电脑想要使用哪一个。

- **切换到特定版本（激活环境）：**

  ```
  conda activate py38
  ```

  *(激活后，命令行最前面会出现 `(py38)` 的字样，说明切换成功。此时输入 `python --version` 会显示 3.8.x)*

- **退出当前版本（回到默认环境）：**

  ```
  conda deactivate
  ```

  *(此时命令行前缀会变回 `(base)`，这是 Anaconda/Miniconda 默认自带的 Python 环境)*



#### 查看系统中已经创建的Python环境

使用以下命令：

```bash
conda env list
```

或者：

```bash
conda info --envs
```

终端中输出结果带`*`的行，表示当前正在使用的环境。



#### 彻底删除某个Python环境

使用命令：

```bash
conda remove -n env_name --all
```



### 使用pip或conda安装编程需要的包或库

`pip` 是 Python **官方**的包管理工具，而 `conda` 是由 **Anaconda 公司**开发的跨平台管理工具。

| **特性**     | **pip**                                | **conda**                                        |
| ------------ | -------------------------------------- | ------------------------------------------------ |
| **定义**     | Python 官方指定的安装工具              | 跨平台的包和环境管理器                           |
| **安装范围** | 仅限 Python 库（如 Pandas, Flask）     | **任何软件**（Python 库、C++ 库、R语言等）       |
| **依赖处理** | 只管 Python 依赖，不管系统底层依赖     | 会自动检查并安装所有相关的底层库（如 MKL, CUDA） |
| **环境管理** | **不支持**。需要配合 `venv` 等额外工具 | **原生支持**。可以随意创建和切换虚拟环境         |
| **生态系统** | 拥有最全最新的包（PyPI 仓库）          | 包的数量略少，但经过严格测试（Conda 仓库）       |
| **安装源**   | 默认从 PyPI 下载                       | 默认从 Anaconda 仓库下载                         |

+ 如果要装一个纯 Python 写的工具，`pip` 很快。

+ 如果要装像 **TensorFlow、PyTorch** 这种涉及复杂底层驱动和 C++ 编译的库，`conda` 会帮你把底层的驱动依赖一并搞定，避免出现“明明装了却报错找不到 DLL”的情况。



#### 使用`pip`

`pip` 通常在默认（系统环境变量配置）的 Python 路径下工作。

- **安装包：**

  ```bash
  pip install 包名      # 示例：pip install requests
  ```

- **安装特定版本：**

  ```bash
  pip install 报名==版本号  # 示例：pip install pandas==1.5.0
  ```

- **卸载包：**

  ```bash
  pip uninstall 包名
  ```

- **查看已安装：**

  ```bash
  pip list
  ```

- **升级包：**

  ```bash
  pip install --upgrade 包名
  ```



#### 使用`conda`

`conda` 建议在特定的虚拟环境下操作。

- **安装包：**

  ```bash
  conda install 包名    # 示例：conda install numpy
  ```

- **在特定环境下安装：**

  ```bash
  conda install -n 环境名 包名
  ```

- **卸载包：**

  ```bash
  conda remove 包名
  ```

- **搜索包（看看仓库里有没有）：**

  ```bash
  conda search 包名
  ```

- **查看当前环境已装：**

  ```bash
  conda list
  ```



#### `pip`与`conda`混用

在实际开发中，我们经常会**混合使用**两者，但请遵循以下原则：

1. **优先使用 `conda`：** 比如你要装 `numpy`, `scipy`, `matplotlib` 等大型科学计算库，先尝试 `conda install`。
2. **`conda` 找不到再用 `pip`：** 有些小众的库或者刚发布的库，Conda 仓库里可能没有，这时候再用 `pip install`。
3. **安装顺序：** 最好先用 `conda` 把大环境搭好，最后再用 `pip` 补齐缺少的包。
4. **注意环境激活：** 使用 `pip` 之前，务必确保你已经 `conda activate` 到了正确的虚拟环境，否则包会装到系统全局路径下去，导致环境混乱。



### 运行Python

#### 在Python的命令行中运行简单的Python程序

在系统的终端中输入执行命令`python`（MacOS或者Linux需要输入`python3`）后回车，如果出现Python的提示符`>>>`，则说明系统找到了安装的Python环境（这个是系统环境变量中配置的）。

在Python的会话中输入`print("Hello World !")`回车，命令行就会执行Python命令打印出`Hello World !`。

按`ctrl+Z`或输入`exit`后按回车，退出Python会话。



### 注释

Python中注释用井号`#`标识，`#`后面的内容会被Python解释器忽略。



### 在系统终端中运行Python程序

新建一个`HelloWorld.py`文件，文件中输入：

```python
print("Hello World !")
```

将文件保存退出。

在系统终端中`cd`到`HelloWorld.py`文件所在目录，执行`python HelloWorld.py`或`python3 HelloWorld.py`（MacOS或Linux系统）命令。

在终端中打印`Hello World !`。



### 使用集成开发环境编写Python程序文件并执行

在集成开发环境（IDE）中编写`HelloWorld.py`文件，保存后点击IDE的运行按钮运行程序即可。



## 变量与基本数据类型

在 Python 中，基本数据类型是构建程序的基础。Python 是一种**动态类型语言**（解释器对变量的类型检查是动态的），这意味着你不需要显式声明变量的类型，Python 会在运行时自动识别。

### 变量

变量命名规则：

1. 变量名只能包含字母`a-z A-Z`、数字`0-9`和下划线`_`，且只能以字母或下划线开头，不能以数字开头。***在Python3中变量名还可以包含其他的Unicode字符，如中文，但是不推荐使用。

2. 变量名不能包含空格，但能使用下划线分隔其中的单词。

3. 不能将Python关键字和函数名用作变量名。查询Python的关键字可以使用`import keyword;  keyword.kwlist`：

   ```python
   ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
   ```

4. 变量名应既简短又具有描述性。

5. 慎用小写字母`l`和大写字母`O`，容易被认作数字`1`和`0`。

在Python中变量视作：可以被赋值的标签，也可以说变量指向特定的值。

```python
name = "张三"  # 字符串
age = 18  # 数字
address = ['中国', '上海', '徐家汇']  # 列表

print(name, age, address)
```

可在一行代码中同时给多个变量赋值，需要使用逗号`,`将变量名分开，对于要赋给变量的值，也需要使用逗号分开。

```python
x, y, z = 0, 1, 2
```



### 基本数据类型

一般将Python的基本数据类型分为5类：数值类型（整数、浮点数、复数），布尔类型，序列类型（字符串、列表、元组），映射类型（字典），集合类型（集合）。

可以使用 Python 内置的 `type()` 函数来检查变量的类型：

```python
x = 10
print(type(x))  # 输出: <class 'int'>

y = [1, 2, 3]
print(type(y))  # 输出: <class 'list'>
```



#### 数值类型(Numeric Types)

用于存储数字。

- **整数 (`int`)**：包含正整数、负整数和零。Python 3 的整数是长整型，没有大小限制。
  - *示例：* `10`, `-5`, `0`
- **浮点数 (`float`)**：带有小数点的数字，也可以用科学计数法。
  - *示例：* `3.14`, `-0.001`, `2e3` (即 2000.0)
- **复数 (`complex`)**：由实部和虚部组成，虚部用 `j` 表示。
  - *示例：* `3 + 4j`

对数值类型的使用和基本计算见本目录下的`./codes/demo01/Numeric.py`文件。

##### 算术运算符

基础四则运算，它们对整数、浮点数、复数都适用：

| 运算符 | 作用     |
| ------ | -------- |
| `+`    | 两数相加 |
| `-`    | 两数相减 |
| `*`    | 两数相乘 |
| `/`    | 两数相除 |

+ 在 Python 3 中，**整数或者浮点数的除法结果永远是浮点数（小数）**，即使是两个整数相除`2/5=0.4`。
+ **复数按照复数的运算规则进行**。

高级运算符，在编程逻辑中非常有用。

| 运算符 | 说明               |
| ------ | ------------------ |
| `%`    | 取模或取余         |
| `//`   | 取整               |
| `**`   | 幂运算，如`2**3=8` |

+ 取模 / 取余 (`%`)：返回除法的余数。常用于**判断奇偶性或循环逻辑**。
+ 整除 (`//`)：返回商的**整数部分**（向下取整），如`7//3=2;-7//3=-3`。
+ 幂运算 / 次方 (`**`)：计算 $a$​ 的 $b$​ 次方，如`2**10=1024`。

运算符优先级（从高到低）：

1. 括号 `()`：最高优先级，用于改变运算顺序。
2. 幂运算 `**`
3. 乘、除、整除、取模 `*`, `/`, `//`, `%`（同一级，按从左到右顺序）
4. 加、减 `+`, `-`

增强赋值运算符——对变量自身进行运算并重新赋值：

| 运算符示例 | 等价    |
| ---------- | ------- |
| `a+=1`     | `a=a+1` |
| `a-=1`     | `a=a-1` |
| `a*=2`     | `a=a*2` |
| `a/=2`     | `a=a/2` |

Python中没有`++`和`--`操作，可用`+=1`和`-=1`代替。



#### 布尔类型(Boolean Type)

用于逻辑判断。

布尔类型的值（布尔值，`bool`）只有两个：

+ `True`（真）
+ `False`（假）

***注意： Python 中布尔值是整数的子类，`True` 相当于 1，`False` 相当于 0。***

布尔值通常是比较运算的结果。

```python
print(1 == 1) # True
print(1 != 1) # False
print(1 > 1) # False
print(1 < 1) # False
print(1 >= 1) # True
print(1 <= 1) # True
```

 有关布尔类型的使用在本目录下的`./codes/demo01/Boolean.py`文件中



##### 比较运算符

| 运算符 | 说明             |
| ------ | ---------------- |
| `==`   | 等于（相等）     |
| `!=`   | 不等于（不相等） |
| `>`    | 大于             |
| `<`    | 小于             |
| `>=`   | 大于等于         |
| `<=`   | 小于等于         |



##### 逻辑运算符——与、或、非

在进行条件判断时可能需要对多个条件进行逻辑运算——“与”运算（同时满足）、“或”运算（满足其中一个）、“非”运算（不满足条件）。

| 运算符 | 说明   | 运算方式                |
| ------ | ------ | ----------------------- |
| `and`  | 逻辑与 | `[表达式] and [表达式]` |
| `or`   | 逻辑或 | `[表达式] or [表达式]`  |
| `not`  | 逻辑非 | `not [表达式]`          |

示例：

```python
#  and
print(True and True) # True
#  or
print(True or False) # True
#  not
print(not True) # False
```



##### “空值”的布尔值

**对于数值`0`、空值`None`、单引号空字符串`''`、双引号空字符串`""`、空列表`[]`、空元组`()`、空字典`()`，Python都会返回`False`**。



#### 序列类型 (Sequence Types)

用于存储有序的一组数据。

##### 字符串（`str`）

用单引号、双引号或三引号括起来的**字符序列**。示例：

```python
string1 = "Hello world!"
string2 = '单引号字符串'
string3 = """（首行）
三引号的
多行
字符串
（末行）"""
```

+ 获取字符串的长度使用`len()`方法，如`len(string1)`。
+ 获取字符串切片（子串）使用`字符串[切片起始位置:切片末尾位置后一位]`，如`string1[2:6]`截取字符串`string1`的第3个字符到第5个字符的子串，在上例中则为`llo`，字符串的第一个字符的位置的下标为`0`。
+ 字符串匹配使用`字符串.find()`，如查找字符串中是否有子串`Hello`使用`string1.find("Hello")`。
+ 字符串大写、小写转换，使用`upper()`、`lower()`方法，如`string1.upper()`，`string1.lower()`。
+ 字符串拼接使用`+`运算符，如`newstr = string1 + string2`。

**说明，字符串是不可变的，所以对字符串使用`upper()`、`lower()`、`+`等方法或运算并不能改变对应字符串的内容，要获取改变后字符串的内容，需要将方法返回值或运算结果赋值给变量。**

如果要在字符串中使用变量，除了通过`+`进行拼接，还可以使用**f字符串**，f是format（设置格式）的简写，变量通过花括号`{}`引用，如`f"你的名字是：{name}"`。

其他的有关字符串的使用在本目录下的`./codes/demo01/Sequence.py`文件中。



##### 列表 (`list`)：

**可变**（Mutable）的序列，可以包含不同类型的元素，这些元素按特定**顺序排列**组成列表，其中的元素之间可以没有任何关系。Python中**使用方括号`[]`表示列表，用逗号`,`分隔其中的元素**。

```python
cities = ["上海", "北京", "广州", "深圳"]
tom_infos = ["Tom", 18, 183.6, True, "slefslehf@lsfef.com"]
cars = [] # 空列表
```

**可以类比C/C++、Java中的数组，只是Python中的列表元素可以是不同类型的值，这与JavaScript的数组又十分相似。**

###### 访问列表元素

列表是有序集合，因此要访问列表的任何元素，只需将该元素的位置（索引）告诉Python即可，类似C/C++、Java中通过数组下标访问数组元素的方式。

```python
print(cities[2]) # 广州
print(tom_infos[-1]) # slefslehf@lsfef.com
```

***在Python中，索引从`0`开始（和很多高级语言一样）；索引`-1`表示最后一个元素或位置。***

###### 修改列表元素

通过元素的索引来为列表中对应元素重新赋值，从而修改列表元素。

```python
cities[0] = "南京"
```

###### 向列表中添加元素

+ 使用`append()`方法在列表的末尾添加新元素，不影响其他所有元素。

  ```python
  cities.append("杭州")
  ```

  使用`append()`使得可以先创建一个空列表，再向列表里面添加元素。

+ 使用`insert()`方法在列表的任意位置添加新元素。

  ```python
  cities.insert(2, "成都")
  cities.insert(0, "中国大陆")
  ```

  **这种操作将列表中在待插入位置右侧的元素都右移一个位置**。

###### 从列表中删除一个元素

+ 使用`del`语句删除元素

  ```python
  del cities[3]
  ```

  使用`del`语句可以删除列表中任意位置的元素，只需要知道其索引即可。

+ 使用`pop()`方法删除元素

  ```python
  last_city = cities.pop()
  ```

  `pop()`方法无参调用将删除列表末尾的元素，并让你能够获取到删除的元素，类似**栈的弹出`pop`（出栈）**。

  `pop()`方法如果使用元素的索引作为参数，将删除列表中对应位置的元素，同样地方法返回删除元素。

  ```python
  first_city = cities.pop(0)
  third_city = cities.pop(2)
  ```

+ 使用`remove()`方法删除列表中指定值的元素

  ```python
  cities.remove("深圳")
  ```

  通过这种方式就不必知道要删除元素的索引信息。

  `remove()`方法只删除列表中出现的第一个指定值的元素，如果列表中有重复值，有一定要将内容一样的元素删除，就需要使用循环来保证每个值都被删除。



###### 判断特定的值是否在列表中

要判断特定的值是否在列表中，可使用关键字`in`。

```python
chars = ['A','B','z','f','t','P']
print("z是否在chars中：", "z" in chars) # z是否在chars中： True
```

如果要判断特定的值不在列表中使用`not in`。

```python
chars = ['A','B','z','f','t','P']
print("a是否不在chars中：", "a" not in chars) # a是否不在chars中： True
```

有关列表的使用可见本目录`./codes/demo01/Sequence.py`文件。



##### 元组 （`tuple`）

**不可变**（Immutable）的序列，一旦创建无法修改。元组看起来和列表很像，但是元组使用圆括号`()`来表示（也可以不使用圆括号），且元组的内容不能修改。

严格来说，元组是由逗号`,`标识的，圆括号`()`只是让元组看起来跟整洁、更清晰，如果**要定义一个只包含一个元素的元组，必须在这个元素的后面加上逗号`,`**（创建只包含一个元素的元组通常没有意义，但自动生成的元组可能只有一个元素）。

```python
seasons = ("春", "夏", "秋", "冬")
months = ("1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月")
weeks = "周一", "周二", "周三", "周四", "周五", "周六", "周日"

one_content = (12)
print(type(one_content)) # <class 'int'>
print(one_content) # 12

one_content = (12,)
print(type(one_content)) # <class 'tuple'>
print(one_content) # (12,)
```



###### 遍历元组中的元素

+ 使用`for`循环遍历

  ```python
  for seanson in seasons:
      print(seanson)
  ```



###### 给元组变量重新赋值

虽然不能修改元组的元素，但可以给表示元组的变量赋值，比如将另一个元组赋值给变量。



#### 映射类型（Mapping Types）

用于存储“键-值”对。

**字典 (`dict`)**：无序（Python 3.7+ 表现为有序）的键值对集合。**键必须是不可变类型（如字符串或数字）**。

在Python中，字典用放在花括号`{}`中的一系列键值对表示。

```python
dict1 = {"name": "Tom", "age": 18, "height": 183.6, "is_married": True, "email": "tom@lsfef.com"}
dict2 = {0: "北京 ", 1: "上海", 2: "广州", 3: "深圳", 4: "杭州", 5: "合肥", 6: "武汉", 7: "长沙", 8: "南昌"} 
dict3 = {} # 空字典
```

键值对包含两个相互关联的值（一个称为“键”，一个称为“值”）。当指定键时，Python将返回与之关联的值。键和值之间用冒号`:`分隔，而键值对之间用逗号`,`分隔。

将多个字典存储在列表中或将列表作为值存储在字典中，称为**嵌套**。可以在列表中嵌套字典，可以在字典中嵌套列表，甚至在字典中嵌套字典。

```python
listIndic = {
    "name": "计算机科学与技术",
    "program_language": ["Python", "C++", "Java", "Rust"]
}
print(listIndic)

dictInlist = [
    {"city": "北京", "code": "0010", "name": "beijing"},
    "上海",
    "深圳",
    "广州"
]
print(dictInlist)

dictIndict = {
    "citis": ["北京", "上海", "广州", "深圳", "重庆", "成都"],
    "university": {
        "北京": "清华大学",
        "上海": "上海交通大学",
        "南京": "南京大学"
    },
    "counts": 158926
}
print(dictIndict)
```

##### 获取字典中的值

+ 通过键名获取对应的值。

  将键名放在字典名后的方括号`[]`中，可以返回键对应的值。

  ```python
  print(dict1["name"])
  print(dict2[2])
  ```

  **注意：如果指定的键名不存在，就将出错。如`print(dict2[100])`**。

+ 通过`get()`方法返回键名对应的值。

  在字典的`get()`方法中依次传入两个参数：指定的键名（必选），当键名不存在时返回的值（可选）。

  ```python
  print(dict1.get("age"))
  print(dict2.get(1))
  print(dict2.get(100))
  print(dict2.get(100, "键名不存在"))
  ```

  如果指定的键名可能不存在，应考虑使用`get()`方法，而是使用方括号`[]`的方式。

  **说明：在调用`get()`方法时，如果没有给出`键名不存在时返回值`参数，Python将返回`None`，这个特殊的值表示没有相应的值。`None`只是一个表示所需值不存在的特殊值**。

##### 添加键值对

字典是一种动态结构，可随时在其中添加键值对，要添加键值对，可依次指定字典名、添加的键名和对应的值。

```python
dict1["gender"] = "male"
dict2[100] = "长春"
```

字典会保留定义时的元素排列顺序，将添加的键值对放在已有元素的后面。

##### 修改字典中的值

要修改字典中的值，可依次指定字典名、修改值对应的键名、修改后的新值。

```python
dict1["name"] = "Jack"
dict2[1] = "香港"
```



##### 删除键值对

使用`del`语句将相应的键值对删除，需要指定字典名和要删除的键名。

```python
del dict1["gender"]
del dict2[100]
```



##### 遍历字典

+ 遍历字典的所有键值对

  使用`for k,v in dict.item()`循环。

  ```python
  for k, v in dict1.items():
      print(k, "::", v)
      
  for num, city in dict2.items():
      print(num, "----", city)
  ```

  示例中`k,v`分别用于存储每次遍历字典元素的键、值，是自定义的变量名。`items()`方法用于返回一个键值对列表。

+ 遍历字典中所有的键

  当不需要值的时候，仅仅获取字典中的键名，可以使用`keys()`方法和`for`循环来遍历字典。

  ```python
  for k in dict1.keys():
      print(k)
  ```

  因为在遍历字典时会默认遍历所有的键，所以仅获取键名时可以省略`keys()`方法，但代码可读性降低。

  ```python
  for num in dict2:
      print(num)
  ```

+ 按特定的顺序遍历字典中的所有键

  要以特定的顺序返回元素，一种办法是在`for`循环中对返回的键进行排序。为此，可以使用`sorted()`函数来获得特定顺序排列的键列表的临时副本。

  ```python
  for k in sorted(dict1.keys()):
      print(k)
  ```

+ 遍历字典中的所有值

  使用字典的`values()`方法，它会返回一个值列表。

  ```python
  for value in dict1.values():
      print(value)
  
  for city in dict2.values():
      print(city)
  ```



#### 集合类型（Set Types）

用于存储无序且**唯一**的元素。

**集合 (`set`)**：可变的无序集合，常用于去重或数学运算（并集、交集）。

集合中的每一个元素都是独一无二的，即**没有重复元素**。

集合使用花括号`{}`表示，元素之间用逗号`,`隔开。

```python
set1 = {1,2,3,4,5,6,7}
set2 = {"Java", "Python", "C++", "C#", "PHP", "JavaScript"}
```

集合看上去和字典很像（都用花括号`{}`括起来），当**花括号`{}`里没有键值对时，定义的很可能是集合**。不同于列表和字典，集合不会以特定的顺序存储元素，即集合是无序的。

集合通常用于去重（去除重复元素）或进行集合运算（交集、并集）。



---

### 数据类型总结

从**“是否可变”**这个重要维度来划分：

| **类型**   | **关键字** | **是否可变** | **例子**   |
| ---------- | ---------- | ------------ | ---------- |
| **整数**   | `int`      | 不可变       | `10`       |
| **浮点数** | `float`    | 不可变       | `3.14`     |
| **复数**   | `complex`  | 不可变       | `4+5j`     |
| **字符串** | `str`      | 不可变       | `"Hello"`  |
| **元组**   | `tuple`    | 不可变       | `(1, 2)`   |
| **列表**   | `list`     | **可变**     | `[1, 2]`   |
| **字典**   | `dict`     | **可变**     | `{"a": 1}` |
| **集合**   | `set`      | **可变**     | `{1, 2}`   |



### input函数

`input()`函数让程序暂停运行，等待用户输入一些文本，通过函数的返回值可以将用户输入赋值给变量。

```python
name = input("请输入你的名字：")
```

`input()`函数接受一个参数——向用户显示的提示（prompt），让用户知道该输入什么样的信息。如果提示的内容超过一行，可以先将提示赋值给一个变量，再将变量作为`input()`函数的参数。关于多行字符串可以使用三个双引号，也可以使用转义字符`\n`（换行）。

```python
prompt = """欢迎使用Python进行编程！
请输入你的名字："""
name = input(prompt)

prompt = f"你好，{name} ! \n请输入你的年龄："
age = int(input(prompt))
```

**在使用`input()`函数时，Python会将用户输入解读为字符串**，所以在获取数值类型时，需要进行类型转换。



## 程序控制结构

Python 的程序控制结构决定了代码的**执行顺序**。

Python 主要有三大类控制结构：**顺序结构**、**分支结构（选择）和循环结构**。

顺序结构：代码按照编写的先后顺序，从上到下逐行执行。



### 分支结构

分支结构根据“条件”是否成立，来决定执行哪一部分代码。

**Python的分支结构严格来说只有`if...elif...else`一种语句，没有类似C/C++、Java的`switch...case`分支语句，有可替代的`match...case`语句（Python 3.10+ 开始），但后者更认为是一种结构化模式匹配（Structured Pattern Matching），其功能比传统的 `switch...case` 强大得多**。

#### if...elif...else语句

这是 Python 处理判断的核心语法。

- **`if`**：如果条件成立，执行。
- **`elif`**：如果前面的条件不成立，但这个条件成立，执行。
- **`else`**：如果以上条件都不成立，执行。

每条`if`语句的核心都是一个值为布尔值（`True`或`False`）的表达式，Python称为`条件测试`.。

##### 单分支：if语句

只有一个条件测试和一个执行序列：

```
if conditon_test:
    do something
    ...
    do something
```

**Python没有C/C++、Java使用`{}`括起来的语句块，Python通过缩进判断语句块，所以`if`条件测试后面的执行代码要使用缩进，建议缩进使用4个空格**。

示例：

```python
num = int(input("请输入数字："))
if num % 2 == 0:
    print("数字是偶数")
```



##### 双分支：if...else语句

在条件测试通过执行一个操作，在条件测试不通过执行另一个操作。

```
if condition_test:
    do something
    ...
else:
    do somethins
    ...
```

示例：

```python
age = int(input("请输入年龄："))
if age >= 18:
    print("已成年")
else:
    print("未成年")
```



##### 多分支if...elif...else语句

当需要检测的测试条件大于两个时，就要使用if...elif...else语句

```
if condition_test1:
    do something
    ...
elif condition_test2:
    do something
    ...
elif condition_test3:
    do something
    ...
...
    ...
elif condition_testn:
    do something
    ...
else: 
    do something
    ...
```

示例：

```python
age = int(input("请输入年龄："))
if age <=0:
    print("年龄输入错误——输入的数字不能小于0")
elif age < 18:
    print("未成年")
elif age <= 30:
    print("青少年")
elif age < 60:
    print("中年人")
elif age < 80:
    print("老年")
elif age < 120:
    print("长寿的人")
elif age <= 140:
    print("老寿星")
else:
    print("确定年龄没有输入错误吗？真是世所罕有的人。")
```



##### 省略else代码块

Python并不要求`if...elif`结构后面必须有else代码块。在一些情况下，`else`代码块很有用；而在其他情况下，使用一条`elif`语句来处理特定的情形更清晰。

```python
age = int(input("请输入年龄："))
if age <= 0:
    print("年龄输入错误——输入的数字不能小于0")
elif age < 18:
    print("未成年")
elif age <= 30:
    print("青少年")
elif age < 60:
    print("中年人")
elif age < 80:
    print("老年")
elif age < 120:
    print("长寿的人")
elif age <= 140:
    print("老寿星")
elif age > 140:
    print("确定年龄没有输入错误吗？真是世所罕有的人。")
```

`else`语句是一条包罗万象的语句，只要不满足任何`if`或`elif`中的条件测试，其中的代码就会执行，这可能引入无效甚至恶意的数据。

如果知道最终要测试的条件，应考虑使用一个`elif`来代替`else`语句。这样就可以肯定，仅当满足相应条件时，代码才会被执行。



### 循环结构

循环结构用于重复执行某段代码，直到满足特定条件为止。

**Python中的循环有`for`循环和`while`循环，但没有`do...while`循环**。

#### for循环

用于**遍历**（依次取出）序列中的每一个元素（如列表、字符串、或数字范围）。**适用场景**：已知循环次数，或者需要处理一个集合。

使用`for`循环对列表、元组、字典等进行遍历在[基本数据类型](#基本数据类型)中已经展示，基本使用格式：

```
for value in [list]|[tuple]|[dict]：
    use value to do something
    ...
```

要使用如 C/C++、Java那样的`for(int i =  0; i < 10; i++){...}`语句，需要了解`range()`函数。

##### range类型

`range`类型用于表示不可变的数字序列，一般用于循环次数特定的`for`循环中。

Python是一个面向对象的程序设计语言，它同样将一切视作对象。`range`类”class“的构造函数`range()`用于创建`range`对象，它有两个构造函数声明：

```python
class range(stop)
class range(start, stop[, step])
```

+ 构造函数的**参数必须是整数**。
+ 如果省略步长`step`参数，**默认步长`step`是`1`**。
+ 如果步长`step`为0，会出现`ValueError`错误。
+ 如果省略起始`start`参数，**默认起始`start`从`0`开始**。
+ 如果步长`step`为正数，构造的`range`对象的内容根据公式确定：`r[i] = start + step * i`，其中`i >= 0`且`r[i] < stop`。也即**步长为正**时，`range()`创建的数字序列是一个**递增序列**，且序列元素不会大于等于`stop`参数。
+ 如果步长`step`为负数，构造的`range`对象的内容仍有公式`r[i] = start + step * i`确定，其中`i >= 0`且`r[i] > stop`。也即**步长为负**时，`range()`创建的数字序列是一个**递减序列**，且序列元素不会小于等于`stop`参数。
+ 在创建数字序列时，如果`r[0]`就不能满足约束：`r[0] < stop`（步长为正）或`r[0] > stop`（步长为负），则创建的数字序列为空（`range`对象没有元素，是一个空的序列）。
+ 注意：**使用`range()`构造函数构造出的对象是`range(start,stop[,step])`形式的对象，需要对它进行类型转换，将它转换为列表或元组类型**。

```python
print("range(5):", range(5), list(range(5)), tuple(range(5)))
# range(5): range(0, 5) [0, 1, 2, 3, 4] (0, 1, 2, 3, 4)

print("range(0):", range(0), list(range(0)),tuple(range(0)))
# range(0): range(0, 0) [] ()

print("range(1,10):", range(1,10), list(range(1,10)))
# range(1,10): range(1, 10) [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("range(1,10,1):", range(1,10,1), list(range(1,10,1)))
# range(1,10,1): range(1, 10) [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("range(1,10,3):", range(1,10,3), list(range(1,10,3)))
# range(1,10,3): range(1, 10, 3) [1, 4, 7]

print("range(10,1,-1):", range(10,1,-1), list(range(10,1,-1)))
# range(10,1,-1): range(10, 1, -1) [10, 9, 8, 7, 6, 5, 4, 3, 2]

print("range(10,-10,-2):", range(10,-10,-2), list(range(10,-10,-2)))
#range(10,-10,-2): range(10, -10, -2) [10, 8, 6, 4, 2, 0, -2, -4, -6, -8]

print("range(5,0,1):", range(5,0,1), list(range(5,0,1)))
# range(5,0,1): range(5, 0) []

print("range(1,2,-1):", range(1,2,-1), list(range(1,2,-1)))
# range(1,2,-1): range(1, 2, -1) []
```



##### 指定循环次

通过`range()`构造函数，在Python中可以实现如 C/C++、Java那样的`for(int i =  0; i < 10; i++){...}`语句。

示例：

```python
for i in range(10):
    print("循环次数：", i)
    
sum = 0
for i in range(0,10,1):
    sum += i
print("0-9求和：", sum)
```



#### while循环

只要条件为 `True`（真），就会一直重复执行。**适用场景**：不知道具体循环多少次，只知道什么时候该停止。

格式：

```
while condition_test:
    do something
    ...
```

示例：

```
content = input("请输入：")
while content != "exit" and content:
    print(type(content), content)
    content = input("请输入：")
    
num = int(input("请输入一个正整数，将计算1到这个数的正整数和："))
sum = 0
while num > 0:
    sum += num
    num -= 1
print(sum)
```

**在Python中没有`do...while`循环，可以使用永真循环（死循环）+`if`语句+`break`语句实现**。



#### 跳出/结束循环

在循环过程中，有时我们需要提前跳出或者跳过某一部分，这时会用到以下三个关键字：

- **`break`**：彻底终止整个循环，直接跳出。
- **`continue`**：跳过本次循环剩下的代码，直接开始下一次循环。
- **`pass`**：空操作，占位符。当你还没想好代码怎么写，但为了语法不报错时使用。

示例：

```python
while True:
    content = input("请输入：")
    if content == "continue":
        continue
    elif content == "break":
        break
    elif content == "pass":
        pass
    else:
        print(content)
```



### match...case语句

`match...case`是Python 3.10版本之后引入的，如果 Python 版本低于 3.10，运行这些代码会直接报 `SyntaxError`错误。

虽然它看起来像其他语言的 `switch`，但 Python 的 `match...case` 实际上叫**模式匹配**，它的功能要强大得多。

#### 简单的值匹配（基础用法）

这种用法最接近传统 `switch` 的用法。

示例：

```python
code = int(input("请输入错误代码："))
match code:
    case 400:
        print("错误代码：400，请求错误")
    case 404:
        print("错误代码：404，未找到")
    case 500:
        print("错误代码：500，服务器错误")
    case _:  # 这是一个通配符，表示匹配“其他所有情况”
        print("未知错误")
```



#### 解构匹配：匹配数据结构 (最强功能)

`match...case` 真正厉害的地方在于它可以直接“拆解”列表、元组或字典。

例如，根据列表的内容和长度来执行不同的逻辑：

```python
command = input("请输入指令（例如：goto 10 20）：").split()
match command:
    case ["quit"]:
        print("退出程序")
    case ["load", filename]:  # 匹配有两个元素，且第一个是 load 的列表
        print(f"正在加载文件：{filename}")
    case ["goto", x, y]:  # 自动把第二、三个元素赋值给变量 x 和 y
        print(f"移动到坐标：({x}, {y})")
    case ["say", *words]:  # *words 匹配剩余的所有内容
        print(f"你说：{' '.join(words)}")
    case _:
        print("无法识别的指令")
```



#### 条件匹配：配合if使用

有时候不仅要匹配结构，还要满足特定条件，可以在 `case` 后面加一个 `if`。

示例：

```python
x = int(input("请输入x坐标："))
y = int(input("请输入y坐标："))
point = (x, y)
match point:
    case (x, y) if x == y:
        print(f"点在对角线上：{x}")
    case (x, y):
        print(f"普通坐标点：({x}, {y})")
```

+ **变量覆盖**：在 `case (x, y):` 中，`x`或`y` 不会去匹配名为 `x` 或`y`的变量的值，而是会变成一个**捕获变量**，匹配任何东西并把值赋给 `x`或`y`。如果你匹配一个已经定义好的变量的值，需要使用 `case` 配合枚举类或 `.` 语法。



#### 匹配对象（类）

甚至可以直接匹配一个类实例的属性。

示例：

```python
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


user = User("Alice", "admin")

match user:
    case User(name=name, role="admin"):
        print(f"管理员 {name} 已登录")
    case User(name=name):
        print(f"普通用户 {name} 已登录")
```



#### 总结

| **维度**       | **match...case**                 | **if...elif...else**       |
| -------------- | -------------------------------- | -------------------------- |
| **匹配对象**   | 复杂数据结构、类型、属性         | 简单的布尔表达式           |
| **代码简洁度** | 高（声明式，自动解构）           | 低（命令式，需手动取值）   |
| **运行环境**   | 仅限 Python 3.10+                | 所有版本                   |
| **主要用途**   | 协议解析、指令分发、复杂对象过滤 | 基础逻辑控制、简单条件判断 |





## 函数

当需要在程序中多次执行同一项任务时，无序反复编写完成该任务的代码，只需要调用执行该任务的函数，让Python运行其中的代码即可。



### 函数定义

在Python中定义函数使用`def`关键字。

格式：

```
def 函数名([函数参数1[,函数参数2[,函数参数3[,...]]]]):
    """函数注释/文文档字符串"""
    函数体
```

示例：

```python
def sum_one_to_num(num):
    """求1到num的整数和"""
    sum = (num / 2) * (1 + num)
    return int(sum)


print(sum_one_to_num(100))
```

+ `def`用来告诉Python要定义一个函数，后面是自己定义的函数名，函数名后的圆括号`()`内写函数处理时需要的参数（可以没有参数，也可以有多个参数），右括号`)`后紧跟冒号`:`，至此函数的定义完成。
+ 紧跟在函数定义后的缩进共同构成了函数体，函数体中可以编写函数的处理过程。
+ 在第二行中用三个双引号`"""`引起来的文本是称为**文档字符串**（docstring）的注释，用来描述函数的功能。Python在为程序中的函数生活文档时，会查找紧跟在函数定义后的字符串。字符串使用三个双引号引起，能够包含多行。
+ 要使用函数就要调用它，通过函数名以及函数参数进行调用。



### 函数参数

函数参数用于向函数传递信息，完成函数功能。函数的参数可以有多个，也可以没有参数。

```python
def print_people(name, age, email, address, gender):
    """打印个人信息"""
    print("Name:", name)
    print("Age:", age)
    print("Email:", email)
    print("Address:", address)
    print("Gender:", gender)
```



#### 形参&实参&默认值

在函数定义时圆括号`()`中的参数称为**形参**；在函数调用时`()`中的参数称为**实参**。

在Python中传递实参有两种方式：**位置实参**和**关键字实参**。

**位置实参**：在调用函数时按照函数定义中形参的顺序给出相应的实参，Python将实参与形参按位置顺序关联。

```python
print_people("Tom", 30, "<EMAIL>", "US", "male")
```

位置实参中实参的顺序很重要。

**关键字实参**：调用函数时传递给函数`名值对`，直接在实参中将参数名称与值关联起来。关键字实参不仅不需要考虑函数调用时的实参顺序，而且清楚地指出了函数调用中各个值的用途。

```python
print_people(name="李明",email="good@a.com",gender="男",age=21,address="北京")
```

在使用关键字实参时，务必准确地指定函数定义中的形参名。

函数**参数默认值**：在函数定义时给形参指定默认值，调用函数时如果没有给出实参，则函数执行时使用参数的默认值。

```python
def draw(size, shape="circle", color="red"):
    """画图形"""
    print(f"The shape is {shape} , its size is {size}, and the color is {color}")


draw(size="large") # The shape is circle , its size is large, and the color is red
draw("100px",color="blue") # The shape is circle , its size is 100px, and the color is blue
```

给形参指定默认值后，可在函数调用中省略相应的形参，不仅能简化函数调用，还能清楚的指出函数的典型用法。

**注意：当使用默认值时，必须在函数定义的形参列表中先列出没有默认值的形参，再列出有默认值的形参，这样Python才能正确的解读位置实参**。即`def draw(shape="circle", color="red", size):`是不正确的，Python会报错。

可以混合使用位置实参、关键字实参以及参数默认值。



#### 传递任意数量的位置实参

有时，不知道函数在调用时需要接受多少个实参，Python允许函数从调用语句中获取任意数量的实参，但要在函数定义时对形参进行处理——在接受任意数量实参的形参名前加一个星号`*`。

```
def 函数名(*形参名):
    do something
    ...
```

示例：

```python
def print_names(*names):
    print(*names)
    print(names)


print_names("Jack","Tom", "Aimy","Bob", "Rose") 
# Jack Tom Aimy Bob Rose
# ('Jack', 'Tom', 'Aimy', 'Bob', 'Rose')
```

+ 形参名`*names`中的星号`*`让Python创建一个名为`names`的**元组**，该元组包含函数收到的所有实参。

如果要让函数接受不同类型的实参，必须**在函数定义中将接纳任意数量实参的形参放在最后**，这点和形参默认值一致。**Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中**。

```python
def print_students(school="Primary School", *students):
    print(school, students)


print_students("Jack", "Tom", "Aimy", "Bob", "Rose") 
# Jack ('Tom', 'Aimy', 'Bob', 'Rose')
print_students("High School")
# High School ()
print_students("High School", "Jack", "Tom", "Aimy", "Bob", "Rose",)
# High School ('Jack', 'Tom', 'Aimy', 'Bob', 'Rose')
```



#### 使用任意数量的关键字实参

有时也希望接受的任意数量的实参能够按照关键字进行接收和处理（接受任意数量的键值对），就要使用任意数量的关键字实参。同样需要在函数定义时，对接受任意数量关键字实参的形参进行处理——在接受任意数量关键字实参的形参名前加两个星号`**`。

```
def 函数名(**形参名):
    do something
    ...
```

示例：

```python
def print_university(**university):
    print(*university)
    print(university)


print_university(name="清华大学", location="北京", built_date="1911-3-30")
# name location built_date
# {'name': '清华大学', 'location': '北京', 'built_date': '1911-3-30'}
```

+ 形参`**university`中的两个星号`**`让Python创建一个名为`university`的**字典**，该字典包含函数接收到的所有关键字参数，并将关键字参数转换为了键值对。
+ 会经常看到有函数的形参名`**kwargs`，它用于收集任意数量的关键字实参。

---

在编写函数时，可以用各种方式混合使用位置实参、关键字实参和任意数量的实参。



### 函数返回值

函数的功能不一定是打印显示信息，还有可能是对一些数据进行加工处理后将结果返回给调用函数的代码，而函数返回的值称为**返回值**。在函数体中，使用`return`语句将函数返回值返回给调用函数的代码。

```python
def sum_one_to_num(num):
    """求1到num的整数和"""
    sum = (num / 2) * (1 + num)
    return int(sum)
```



### 模块

将函数存储在称为**模块**的独立文件中，再将模块导入主程序，就可以在主程序中使用模块中定义的函数，这样可隐藏程序代码的细节，将重点放在程序的高层逻辑上。

模块就是文件扩展名为`.py`的文件，包含要导入程序的代码。

模块的使用步骤：

1. 新建一个模块——新建一个`.py`文件，文件名自定义，这里用`module_name`指代。
2. 在模块中定义、编写被重复调用的函数——这里用`function_name`指代
3. 在需要调用模块的代码文件或主程序文件（同样是`.py`文件）中使用`import`语句导入模块及其函数
4. 调用模块中的函数



**模块的导入及函数调用**有以下几种方式：

+ 导入整个模块：`import module_name`
  + 调用模块中的函数——使用句号`.`隔开模块名和函数名：`module_name.function_name()`
+ 导入模块中特定的函数：`from module_name import function_name1, function_name2, function_name3`，导入多个函数使用逗号`,`分开不同的函数名
  + 调用模块中的函数——直接通过函数名调用：`function_name1()`，因为在`import`语句中已经显式导入了函数，所以无须再使用句号`.`分隔
+ 给导入的模块指定别名（alias）：`import module_name as alias`
  + 调用模块中的函数——使用句号`.`隔开模块的别名和函数名：`alias.function_name()`
+ 给导入的特定函数指定别名（alias）：`from module_name import function_name as alias`
  + 调用模块中的函数——直接通过函数的别名调用：`alias()`
+ 导入模块中所有的函数：使用星号`*`可以让Python导入模块中所有的函数，`from module_name import *`
  + 调用模块中的函数——因为导入了模块中的每一个函数，所以直接通过函数名调用即可，无须使用句号`.`：`function_name()`

**为了提高代码的可理解性和可读性，建议要么只导入需要使用的函数，要么导入整个模块并使用句号`.`调用函数，这能让代码更清晰，更容易理解和阅读**。



### 函数编写指南

在编写函数时，可以参考以下建议或指南：

1. 应给函数指定描述性名称，且只使用小写字母和下划线。模块命名同样遵循上述约定。
2. 每个函数都应该包含简要阐述其功能的注释。该注释紧跟在函数定义后面，并采用文档字符串的格式。
3. 给形参指定默认值时，等号的两边不要有空格；调用函数时使用关键字实参时也一样。这点一般编辑器的格式化工具可以提供自动代码格式化功能。
4. 所有的`import`语句都应放在文件开头，除非要在文件的开头使用注释来描述整个程序。



## 面向对象编程

面向对象编程（Object-Oriented Programming，OOP）是最有效的软件编写方法之一。在面向对象编程中，编写现实世界中的事物和场景的类（class），并基于这些类来创建对象（object）。根据类来创建对象称为实例化，这让你能够使用类的实例（instance）



### 类的定义与实例化

在面向对象编程中，一个类具有属性（字段）——类的数据信息，方法（函数）——类的行为动作。为了能够实例化类的对象，类中还有一种特殊的方法（函数）——构造方法（函数），用于初始化类的实例对象。

Python中一个类的定义语法（格式）：

```
class Class_name:
    """对类的描述"""
    
    def __init__(self, property...):
        self.property = property
        self.property... = property...
    
    def do_thing(self):
        return self.property..
```

实例，一个形状类`Shape`，它包含属性：`size`——大小（`small`、`medium`、`large`），`color`——颜色；方法：`draw()`——画出形状，`changeSize()`——改变大小，`changeColor()`——改变颜色。

```python
class Shape:
    """形状类"""

    def __init__(self, size, color):
        self.size = size
        self.color = color

    def draw(self):
        print(f"This shape: size is {self.size}, color is {self.color}.")

    def changeSize(self, size):
        self.size = size

    def changeColor(self, color):
        self.color = color
```

+ 定义类使用`class`关键字，类名通常首字母大写。定义类之后是一个文档字符串用于对类进行注释。
+ 每一个类都有一个`__init__()`函数（两边有两个下划线`__`），这就是类的构造函数，构造函数在实例化类的对象时被Python自动运行。构造函数一般用于初始化类的属性，所以需要有形参设置属性。
+ 构造函数`__init__()`中第一个形参必须是`self`，且必不可少。当Python调用构造函数`__init__()`实例化类的对象时，将自动传入实参`self`。在类的方法中通过`self.`的方式可以访问类的属性和方法。
+ 每个与实例相关联的方法调用都会自动传递实参`self`，该实参是一个指向实例本身的应引用，让实例能够访问类中的属性和方法。

要对一个类进行实例化的语法格式：`instance = Class_name(property...)`。如实例化一个形状`Shape`类：

```python
shape = Shape("large", "red")
```

实例化对象后，访问对象的属性和调用对象的方法的语法格式：`instance.perperty`和`instance.function()`。

```python
print(shape.size, shape.color)
shape.draw()
shape.changeSize("small")
```

有些属性不需要在构造函数`__init()__`中通过形参来定义，可以指定其默认值。如在`Shape`类中新增属性`area`——面积，默认值为`0`；新增方法`getArea()`——获取形状的面积。

```python
    def __init__(self, size, color):
        self.size = size
        self.color = color
        self.area = 0
        
    def getArea(self):
		return self.area
```

修改实例化对象的属性有两种方式：

+ 直接修改对象的属性：`instance.property = newValue`，如`shape.size = "medium"`
+ 通过类提供的修改属性的方法：`instance.setProperty(newValue)`，如`shape.changeColor("yellow")`



### 继承

当一个类继承另一个类时，将自动获得后者的所有属性和方法。原有的类称为父类（parent class）或超类（super class），新的类称为子类（child class）。子类不仅继承父类的所有属性和方法，还可以定义自己的属性和方法

子类定义时在类名后面加上圆括号`()`，括号内写父类的类名即可。语法格式：`class Class_chird(Class_parent):`。

如定义一个圆类`Circle`，它有自己的新属性：`radius`——半径，`center`——圆心。

```python
class Circle(Shape):
    """圆形类"""

    def __init__(self, size, color, radius, center):
        self.size = size
        self.color = color
        self.radius = radius
        self.center = center
        self.area = 3.14 * (radius ** 2)
```

在上面的代码里，子类的构造函数`__init__()`对父类已有属性一个个初始化很累，可以考虑在子类的构造函数中调用父类的构造函数完成属性初始化。

要**在子类中调用父类的方法，通过`super()`函数**。如：

```python
class Circle(Shape):
    """圆形类"""

    def __init__(self, size, color, radius, center):
        super().__init__(size, color)
        self.radius = radius
        self.center = center
        self.area = 3.14 * (radius ** 2)
```



实例化一个圆`circle`，调用父类已有的方法`draw()`、获取它的面积属性`area`：

```python
circle = Circle("small","blue",4,(0,0))
circle.draw() # This shape: size is small, color is blue.
area = circle.area
print(area) # 50.24
```

方法`draw()`打印的信息和此时子类`Circle`有些不合适，可以通过重写父类的方法，让方法更适合子类使用。

重写父类的方法很简单：在子类中定义一个与要重写父类方法同名的方法即可。如重写`draw()`方法：

```python
    def draw(self):
        print(f"This shape is Circle: radius is {self.radius}, center is {self}, size is {self.size}, color is {self.color}.")
```



### 对象作为类的属性

有时随着类中的属性和方法越来越多，文件也越来越长，一个类变得很“臃肿”，这时可以尝试将类中的一部分属性和方法提取出来作为一个独立的类，然后将这个独立的类作为其他类的一个属性。

将大型类拆分成多个协同工作的小类，这种方法称为**组合**。

如将`Shape`类中的`size`和`color`属性、`changeSize()`和`changeColor()`方法提取成一个外观类`Appearance`:

```python
class Appearance:
    """外观类"""

    def __init__(self, size, color):
        self.size = size
        self.color = color

    def changeSize(self, size):
        self.size = size

    def changeColor(self, color):
        self.color = color
```

将`Shape`类中的代码进行修改——与`size`和`color`属性相关的操作使用`Shape`类新的`appearance`属性完成：

```python
class Shape:
    """形状类"""

    def __init__(self, size, color):
        self.appearance = Appearance(size, color)
        self.area = 0

    def draw(self):
        print(f"This shape: size is {self.appearance.size}, color is {self.appearance.color}.")
        
        
class Circle(Shape):
    """圆形类"""

    def __init__(self, size, color, radius, center):
        super().__init__(size, color)
        self.radius = radius
        self.center = center
        self.area = 3.14 * (radius ** 2)

    def draw(self):
        print(
            f"This shape is Circle: radius is {self.radius}, "
            f"center is {self.center}, size is {self.appearance.size}, color is {self.appearance.color}.")
```

+ 在`Shape`类中定义了一个新的属性`appearance`，它是`Appearance`类的一个实例，在`Shape`类的构造函数`__init__()`中通过`Appearance()`进行实例化，将实例对象赋值给属性`appearance`。



### 导入类

类和函数、其他的Python代码一样都编辑保存在`.py`文件中，将类相关的代码抽取出来存放到独立的`.py`文件中，就可以向[模块](#模块)章节中导入函数一样在其他的`.py`文件使用`import`语句导入需要使用的类。

通过将类存储在模块中，然后在主程序中导入所需的模块（类），能使得文件尽量整洁。

和一个模块中可以定义多个函数一样，一个模块中可以存储多个类，但建议无论是函数还是类都尽量把具有某种相关性的函数或类放在一个模块中。

+ 导入单个类：`form module_name import class_name`
+ 导入多个类：`form module_name import class_name1, class_name2, class_name3, ...`
+ 导入整个模块：`import module_name`
+ 导入模块中所有的类：`from module_name import *`，不建议使用这种方法

根据导入方式的不同，可以直接通过类名或者`模块名.类名`的方式使用导入的类，一般代码编辑器会有自动补全功能。



### 类的编程风格

+ 类名应采用**驼峰命名法**，即类名中的每个单词首字母大写，并且不使用下划线。
+ 实例名和模块名都采用小写格式，并在单词之间加下划线。
+ 对于每个类，都应在类定义后面紧跟一个文档字符串。这种文档字符串简要地描述类的功能。
+ 每个模块也都应该包含一个文档字符串，对其中的类可用来做什么进行描述。
+ 在一个类中可以使用一个空行来分隔方法；在一个模块中，可以使用两个空行来分隔方法。
+ 当要同时导入标准库中的模块和自定义的模块时，先导入标准库中的模块，空一行，再导入自定义的模块。这种做法可以让人更明白使用的各个模块来自哪里。



## Python标准库

Python标准库是一组模块，在安装Python时已经包含在内。如果要使用标准库中的任何函数和类，只需在程序开头添加一条`import`语句即可。

### random模块

+ `randint()`函数：使用两个整数作为参数，并随机返回一个介于两个整数之间（包含）的整数。

  ```python
  from random import randint
  
  print(randint(1, 15))
  ```

+ `choice()`函数：将一个元组或列表作为参数，并随记返回其中的一个元素。

  ```python
  from random import choice
  
  tuple1 = ("花", "草", 1, 3, "ABC", "good")
  print(choice(tuple1))
  list1 = [1, 2, 25, 64, 0, 3, "Night", "world"]
  print(choice(list1))
  ```



## 文件和异常

学习处理文件和保存数据能够让程序更易于使用：用户能够选择输入什么样的数据以及在什么时候处理输入；用户使用程序做完一些工作后，可将程序先关闭，以后再接着往下做。

学习处理异常可以帮助应对文件不存在等情况，以及处理其他的可能导致程序崩溃的问题。这让程序在面对错误数据时更稳健——不管这些错误数据源自无意的错误，还是处于破坏程序的恶意企图。

下面以最基本的文本文件`.txt`进行学习。



### 读取文件

要使用文本文件中的信息，首先需要将信息读取到内存中。既可以一次性读取文件的全部内容，也可以逐行读取。

读取文件的步骤：找到文件 → 打开文件 → 读取文件内容。

+ 找到文件需要将文件的路径告诉Python。Python提供`pathlib`模块，能轻松地在各种操作系统中处理文件和目录。首先从`pathlib`模块中导入`Path`类，`Path`对象指向一个文件。文件路径的表示有绝对路径和相对路径两种。
+ 打开文件读取内容使用`Path`对象的`read_text()`方法——读取文件的全部内容，将文件内容作为字符串返回。再使用字符串的`splitlines()`方法可以将冗长的字符串转换为一系列的行，通过`for`循环可以每次一行的获取文件的内容（实际文件的内容是一次全部读取了）。

示例：

```python
from pathlib import Path

file_path = Path("poem.txt")
contents = file_path.read_text(encoding="utf-8")
# 读取全部内容
print(contents)
# 逐行获取内容
i = 1
for line in contents.splitlines():
    print(f"第{i}行内容：", line)
    i += 1
```

+ 在创建`Path`类对象时传入文件的路径，实例化的对象将指向文件。
+ 调用`Path`对象的`read_text()`方法时，可以指定读取文件的解码格式，若不给定参数则使用默认的解码格式——默认使用系统的默认字符编码（如中文Windows通常是 GBK）。当文件的编码格式和读取文件的解码格式不一致时可能出现乱码，也可能出现`UnicodeDecodeError`异常。

**Python提供的读取文件的库、类、方法有很多，可以根据使用情况选择合适的库、类、方法，不必局限于`pathlib`库中的`Path`类及其方法**。



### 写入文件

与读取文件类似，写入文件的步骤：找到文件 → 打开文件 → 向文件写入内容。

使用`pathlib`库中的`Path`类的`write_text()`方法将信息写入文件。

**注意：当指定文件不存在时，`write_text()`方法会创建文件，然后写入内容。`write_text()`方法写入文件的方式是覆盖（将原文件内容清空后写入新内容）**。

示例：

```python
# 文本文件写操作
from pathlib import Path

file_path = Path("poem01.txt")
contents = "秋浦歌十七首（其十四）\n"
contents += "李白\n"
contents += "炉火照天地，红星乱紫烟。\n"
contents += "赧郎明月夜，歌曲动寒川。"
file_path.write_text(contents, encoding="utf-8")
```

**如果要以追加的方式写入文件，可以使用其他的库、类、方法**。



### 异常

Python使用称为**异常**（`exception`）的特殊对象来管理程序执行期间发生的错误。每当发生让Python不知所措的错误时，Python会创建一个异常对象。如果未对异常进行处理，程序将停止，并显示一个`traceback`，其中包含有关异常的报告。

对异常的处理使用`try...except`代码块。`try...except`代码块让Python执行特定的操作，同时告诉Python在发生异常时应该怎么办。

语法格式：

```
try:
    do something
except ExceptionOne:
    deal with ExceptionOne
except ExceptionTwo:
    deal with ExceptionTwo
except ...:
    ...
else:
    succeed doing something
```

Python执行`try:`后面的代码块时如果发生异常，根据异常类型去匹配`except`代码块，执行对应`except`代码块中处理异常的操作。如果`try:`代码块正常运行，则执行`else:`后面的代码块（`else`并不是必须的）。

示例：

```python
a = int(input("请输入被除数："))
b = int(input("请输入除数："))
try:
    c = a / b
except ZeroDivisionError:
    print("除数不能为0！")
else:
    print("运行无异常。")
    print(f"{a} / {b} = {c}")
```

+ `ZeroDivisionError`是一个异常类，继承自`ArithmeticError`类。`ArithmeticError`类继承自`Exception`类。`Exception`类继承自`BaseException`类。`BaseException`类继承自`object`类。

  `Exception`类：所有非退出（`non-exit`）异常的共同基类。`BaseException`类：所有异常的共同基类。

  所以如果要自定义一个异常类，可以使它继承自`Exception`类。

+ 如果在处理异常时不做任何操作，可以使用`pass`执行空操作。



### 存储数据

一般程序从用户输入获取信息，当用户关闭程序时，几乎总是要保存用户提供的信息。

可以使用文本文件进行保存，但是文本文件的数据一般没有很强的结构性，读取数据的结构信息取决于编写文件写入代码的编程人员，这使得文本文件的可共享性很差。

一种简单的可以在不同程序间、不同编程语言间共享的数据格式就是**JSON**（JavaScript Object  Notation），它虽然最初是为了JavaScript开发的，但后来成为了一种通用的数据格式。

在Python使用`json`模块能够将简单的Python数据结构转换为JSON格式的字符串。

+ `json.dumps()`函数：接受一个实参——即要转换为JSON格式的数据，函数返回一个字符串——数据转换后的JSON字符串。
+ `json.loads()`函数：将一个JSON格式的字符串作为参数，并返回一个Python的对象。

如果要持久化存储数据，可以将数据转换后的JSON字符串写入`.json`文件中，或者从`.json`文件中读取JSON字符串后转换为Python对象。

示例：

```python
# 简单的数据
names = ["Ton", "John", "Smith"]
json_str = json.dumps(names)
# 写入文件
json_file = Path("simple.json")
json_file.write_text(json_str, encoding="utf-8")
# 从文件读取
json_str = json_file.read_text(encoding="utf-8")
names = json.loads(json_str)
print(names) # ["Ton", "John", "Smith"]

# 对象数据
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = People("Ton", 20)
json_str = json.dumps(people.__dict__)
# 写入文件
json_file = Path("people.json")
json_file.write_text(json_str,encoding="utf-8")
# 从文件读取
json_str = json_file.read_text(encoding="utf-8")
people = json.loads(json_str)
print(people) # {'name': 'Ton', 'age': 20}
```



**有关JSON序列化的使用可以查阅有关文档或教程，自行搜素使用**。



## 设置`.py`文件执行入口

Python是一种脚本语言，所以Python对`.py`文件中的代码是从第一行开始逐行执行的。在单文件或者少量文件（模块）导入使用的情况下，程序执行的流程还是很清晰的，不太会出现莫名执行的代码。可随着项目文件数量增加、文件（模块）之间相互导入调用的情况增多，在程序执行的过程中就会出现某些`.py`文件中不希望执行的代码被执行的情况。如：在`sum.py`文件中定义了求两数之和的函数`sum_two()`，接着在`sum.py`文件中编写测试函数功能的代码`print(sum_two(3,4))`。现在在另一个文件`app.py`中使用`from sum import sum_two`导入指定的`sum_two()`函数，运行`app.py`文件时就会在控制台看到打印显示了`7`。

`sum.py`文件：

```python
def sum_two(a, b):
    return a + b

print(sum_two(3,4))
```

`app.py`文件：

```python
from sum import sum_two

print(sum_two(10, 20))
```

控制台显示：

```
7
30
```

显然，在运行`app.py`文件时并不想执行`sum.py`文件中用于测试函数`sum_two()`的代码。因此，需要设置`sum.py`文件的执行入口，当单独执行`sum.py`文件时运行入口之后的代码；当`sum.py`作为模块导入到其他文件时，不执行入口之后的代码，如测试代码等。



### `.py`文件内置变量`__name__`

在 Python 中，`__name__` 是一个非常特殊的**内置字符串变量**。它的核心作用是让程序知道：**当前的 `.py` 文件是被作为“主程序”直接运行，还是被作为“工具插件（模块）”导入到其他文件中运行的。**

Python对`__name__`变量的工作机制：

+ 直接运行`.py`文件时：Python 解释器会自动将该脚本文件的 **`__name__` 变量赋值为 `"__main__"`**。
+ 作为模块导入运行`.py`文件时：**`__name__` 的值被自动赋值为文件（模块）名**。

例如分别在`sum.py`文件和`app.py`文件中添加打印变量`__name__`的代码`print(__name__)`，再运行文件。

单独运行`sum.py`时打印`__main__`；将`sum`导入`app.py`后运行`app.py`，先打印`sum`，再打印`__main__`。



### 设置执行入口

了解了`__name__`这个文件的内置变量之后，可以结合`if`条件语句设置`.py`文件的入口，通过设置入口来保护`.py`文件中的脚本代码不会在被导入时自动执行。

格式：

```
if __name__ == "__main__":
    really doing
```

如在`sum.py`中将测试函数`sum_two()`的代码让在入口中：

```python
def sum_two(a, b):
    return a + b


if __name__ == '__main__':
    print(sum_two(3, 4))
```

接着运行`app.py`文件，控制台就不会打印`7`了，也就是没有执行`sum.py`中的函数测试代码。

假设有一天`app.py`也作为模块被导入进其他的`.py`文件，同样不想执行无关的代码，所以在`app.py`文件也要设置入口：

```python
from sum import sum_two

if __name__ == "__main__":
    print(sum_two(10, 20))
```



**总结：无论编写的`.py`文件此时此刻是否会被其他文件导入，良好的编程习惯是将本`.py`文件要执行的代码统一放置在入口`if __name__ == "__main__":`中**。

使用入口的好处及用途：

1. **编写库文件**：既可以作为模块给别人用，也可以在文件末尾写一些 Demo 或测试用例，不影响别人调用。
2. **防止代码重跑**：避免在多进程编程（`multiprocessing`）中，子进程反复启动主程序逻辑导致死循环。
3. **脚本化工具**：方便将一系列函数封装成可以通过命令行直接调用的工具。

