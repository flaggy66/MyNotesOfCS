# JavaScript基础

## 变量

### 基础

```js
// 变量，创建后可以修改值
let sum=100;
var str="hello";
// 常量，创建后将无法修改值
const MAX=999;

// 同时声明多个变量
let a,b = 0,c = 'abc';

```

希望定义的变量值在创建后可以修改使用`let`关键字或`var`关键字；希望定义的变量值在创建后不被修改使用`const`关键字。

使用等号`=`和一个值来为变量或常量赋值。

上例中赋值完成后修改`MAX`值，如`MAX=1000;`将报错：`TypeError: Assignment to constant variable.`。

如果仅仅只是声明一个变量，没有给它赋值初始化，则它是一个`undefined`值，如`var name;`。

使用`var`和`let`的区别：

1. `var`关键字可以进行”**变量提升**“，`let`关键字只能有限地“提升”。

   直接运行下面的代码：

   ```
   name = "Jack";
   console.log(name);
   ```

   说明：`name`变量之前没有进行任何声明和初始化，直接运行上述代码，不会报错，控制台可以打印输出`Jack`。由此可见，虽然没有使用`var`或`let`关键字声明`name`变量，但是JavaScript还是可以将`name`作为变量进行访问（**这是因为在非严格模式（默认）下，当给一个“未声明的变量”赋值时，JavaScript会自动在全局对象上创建一个属性，浏览器环境则为`window.name="Jack"`，Node.js环境则为`global.name="Jack"`**）。

   增加下述代码的第3行，直接运行：

   ```js
   name = "Jack";
   console.log(name);
   var name;
   ```

   说明：运行结果在控制台打印输出`Jack`。第3行是对变量`name`进行了声明。这里对变量`name`进行了“提升”——将对`name`变量的声明提前了，在代码执行前，JavaScript 引擎会先“扫描”代码，把变量和函数的声明加入到作用域中。需要注意：**提升的是声明，而不是赋值。**

   若将第3行的`var`关键字替换为`let`关键字，运行则将直接报错。

   ```js
   name = "Jack";
   console.log(name);
   let name
   
   /*
   报错：
   Uncaught ReferenceError ReferenceError: Cannot access 'name' before initialization
   */
   ```

   说明：本次运行，第2行的打印输出结果也没有，直接就报错了。通过报错信息可以很清晰地知道，变量`name`“没有被初始化前不能访问”，详细的报错会指出产生报错的位置是第1行。这是因为`let`关键字其实也对变量`name`的声明进行了提前，即JavaScript把变量的声明已经加入到作用域中了，但是和`var`关键字不同的是，`let`关键字限定了对变量`name`的访问区（暂时性死区），在变量`name`被`let`真正声明前不可对变量`name`进行访问，访问就直接报错。简单理解就是**`name`变量虽然已经存在于作用域，但在声明前不可用**。

   **有关变量提升的更多细节问题请自行搜索。**

2. `let`关键字不能对名称相同的变量多次声明，`var`关键字可以。

   如下面的代码将直接报错：

   ```js
   let age = 18;
   let age = 19;
   
   // 使用Node.js报错信息：SyntaxError: Identifier 'age' has already been declared
   ```

   说明：在Node.js环境中运行产生的报错是语法错误，提示`age`变量已经被声明了。

   使用`var`关键字则不会报错：

   ```js
   var age = 20;
   var age = 21;
   ```

   使用`let`关键字只能对同个变量重新赋值：

   ```js
   let age = 18;
   age = 19;
   ```

3. 建议使用`let`关键字，虽然`let`关键字比起`var`关键字有一些限制，但是它可以使代码更易维护。



### 变量命名规则

JavaScript的变量名（标识符）由拉丁字母（0-9、a-z、A-Z）和下划线（_)组成，且不能以数字0-9开头。

一般在命名时遵循如下规则：

1. 变量名不要以数字`0-9`和下划线`_`开头。
2. 变量名采用“小驼峰命名法”，当变量名由多个单词组成时，小写整个命名的第一个字母然后大写剩下单词的首字符。
3. 变量名是大小写敏感的，比如`name`和`Name`是两个变量的名称。
4. 变量名应该直观，它们描述了所包含的数据。即具有一定的语义，不要只使用单一的字母/数字，或者长句。
5. 避免使用 JavaScript 的保留字给变量命名。



## 数据类型

JavaScript 是一种“弱类型、动态类型语言”，这意味着不同于其他一些语言 (如 C/C++、Java)，你不需要指定变量将包含什么数据类型（例如 number 或 string）。

要检查一个变量是什么类型可以使用`typeof 变量名`，如：

```js
let arg1 = "2";
console.log(typeof arg1); // string
arg1 = 2;
console.log(typeof arg1); // number
```

需要强调：***在 JavaScript 中，一切东西都可以被当作对象。***



### Number

不论这些数字是像 30（也叫整数）这样，或者像 2.456 这样的小数（也叫做浮点数）。

```js
let num1 = 100;
let num2 = 3.14159;
let num3 = 3+9;
```



一些关于Number的使用：

+ 保留小数点后几位（四舍五入），使用`Number`的`toFixed()`方法，如3.14159保留三位：`let PI = 3.14159; PI.toFixed(3);`，结果为`3.142`。
+ 将一个字符串数值转换为Number，如将字符串`"25"`转换为`25`，`Number("25");`



### String

在 JavaScript 中，给一个变量赋值为字符串时，你可以选择单引号（`'`）、双引号（`"`）或反引号（```）来包裹字符串，否则 JavaScript 将会把这个字符串值理解成别的变量名。

```js
let str1 = 'hello';
let str2 = "Have a good time !"
let str3 = `This is a dog.`
```

字符串的开头和结尾必须使用相同的字符，否则会出现错误：

```js
let str1 = 'hello"; // 会出现错误
```

使用单引号（''）声明的字符串和使用双引号（""）声明的字符串是相同的，可以根据个人偏好来使用。但推荐选择一种样式并在代码中保持一致。

使用反引号（``）声明的字符串是一种特殊字符串，被称为**模板字面量**。在大多数情况下，模板字面量与普通字符串类似，但它具有一些特殊的属性：

+ 可以在其中嵌入JavaScript。在模板字面量中，可以在 `${ }` 中包装 JavaScript 变量或表达式，其结果将被包含在字符串中。

  ```js
  let name = "小明";
  let words = `你好，${name}`;
  console.log(words); //你好，小明
  let result = `3+5=${3+5}`;
  console.log(result); // 3+5=8
  ```

+ 可以声明**多行**的模板字面量。模板字符串会保留源代码中的换行符，因此可以编写跨越多行的字符串，而使用普通字符串获得等效的输出，你必须在字符串中包含换行字符（`\n`）。

  ```js
  // 多行的模板字面量
  let sentence1 = `10月1日，天气晴，气温19摄氏度。
  今天我要去天安门看升旗仪式！
  ……
  我今天过得很充实！`;
  console.log(sentence1);
  
  // 等效的普通字符串
  let sentence2 = "10月1日，天气晴，气温19摄氏度。\n今天我要去天安门看升旗仪式！\n……\n我今天过得很充实！";
  console.log(sentence2);
  ```

  

很多时候需要对字符串进行拼接，可以使用模板字面量，也可以使用`+`运算符。

```js
let str4 = "Wow!";
let str5 = "So beautiful!";
// 模板字面量
console.log(`${str4}${str5}`);
// + 运算符拼接
console.log(str4+str5);
```

有时字符串中需要包含实际的引号，比如`She said,"This is mine!"`。通常有两种方式：1.使用其他的引号去声明字符串；2.使用转义字符（`\`+`引号`）将引号作为普通的字符而不是字符串声明。

```js
let str6 = 'She said,"This is mine!"'; // 或者用反引号`She said,"This is mine!"`
console.log(str6);
let str7 = "She said,\"This is mine!\"";
console.log(str7);
```

直接将一个Number和一个String拼接，JavaScript会将Number自动转换为String进行拼接。

```js
let money = 100000000;
let dream = "我的存款为：";
console.log(dream + money + "元"); // 我的存款为：100000000元
```

要将一个数值转换为字符串，也可以使用`String()`方法。

```js
String(money);
conole.log("类型：",typeof(money),"值：",money); // 类型： number 值： 100000000
```

String类型自身提供了很多属性和方法便于使用字符串。以`let str8 = "Apple is a fruit.Maybe also is a mobile phone brand."`为例：

```js
// 获取字符串长度：字符串中包含的字符个数，包括空格、换行符等。
str8.length; // 52

// 检索特定字符串字符，比如检索第1个字符（第1个字符的下标为0）
str8[0]; // A
str8[52]; // undefined ，越界访问为undefined

// 查找字符串中特定子串首字符起始下标
str8.indexOf("App"); // 0
str8.indexOf("Mac"); // -1 ，子串不存在返回-1

// 提取字符串中特定下标范围的子串，提取从第一个位置开始，直到但不包括最后一个位置。
str8.slice(0, 5); // Apple ，第一个参数为开始提取的字符位置，第二个参数是提取的最后一个字符的后一个位置。

// 提取从某个位置开始的剩余所有字符组成的子串
str8.slice(46); // brand.

let str9 = str8.slice(0, 5);
// 将字符串中所有字符大写
str9.toUpperCase();
// 将字符串中所有字符小写
str9.toLowerCase();

// 将字符串中某个子串用另一个子串替换
str8.replace("Apple", "Banana"); // Banana is a fruit.Maybe also is a mobile phone brand. 注意：实际str8的字符串内容没有改变
str8 = str8.replace("Apple", "Banana"); // 修改str8的字符串内容为替换后的字符串
```



### Boolean

Boolean 的值有 2 种：`true` 或 `false`。它们通常被用于在适当的代码之后，测试条件是否成立。

```js
let isMale = true;
let open = false;

// 比较运算的结果就是Boolean值。
let result = 6 > 3;
```



### Array

数组是一个单个对象，其中包含很多值，方括号`[ ]`括起来，并用逗号`,`分隔数组元素。

```js
let season = ['spring','summer','fall','winter']
let numArray = [1,20,25,4,36,9,6,58];

// JavaScript中数组元素可以是不同的类型
let arr = [1, "hello", true, 0.123, "world !"];
```

**可以将任何类型的元素存储在数组中，比如字符串、数字、对象、另一个变量，甚至另一个数组。这与C/C++、Java不同。**

要访问某个元素，可以通过数组下标访问。

```js
console.log(season[2]); // fall
console.log(numArray[3]); // 4
console.log(arr[0]); // 1
console.log(arr[5]); // undefined
console.log(arr.length); // 5
```

数组中第一个元素的下标为`0`；下标越界后不会报错，而是将越界访问的元素看作`undefined`；要获取数组的长度（元素的个数），通过数组的属性`length`获得。

数组中包含数组的话称之为多维数组，可以通过将两组方括号链接在一起来访问数组内的另一个数组。

```js
let matrix = [ [1, 2, 5, 8], [3, 4, 6, 7], [9, 10, 11, 12] ];
console.log(matrix[1][2]); // 6
```

字符串与数组的转换：

+ 将字符串转换为数组：

  ```js
  let nameStr = "Jack, Tom, John, Mike";
  let nameArr = nameStr.split(","); // 使用逗号,进行分隔
  console.log(nameArr); // ['Jack', ' Tom', ' John', ' Mike']
  ```

+ 将数组转换为字符串：

  ```js
  let courseArr = ["数学", "英语", "语文"];
  let courseStr1 = courseArr.join(","); // 使用逗号,将数组元素拼接为字符串
  console.log(courseStr1); // 数学,英语,语文
  let courseStr2 = courseArr.toString(); // 直接使用逗号,拼接
  console.log(courseStr2); // 数学,英语,语文
  ```

对一个数组添加和删除元素：

```js
// 添加元素
courseArr.push("物理"); // 在数组末尾添加一个元素
let newLength = courseArr.push("地理", "历史", "生物"); // 在数组末尾添加多个元素
console.log(courseArr); // ['数学', '英语', '语文', '物理', '地理', '历史', '生物']
console.log(newLength); // 7 ，push()方法返回数组的新长度
newLength = courseArr.unshift("化学", "政治"); // 在数组首部添加多个元素
console.log(courseArr); // ['化学', '政治', '数学', '英语', '语文', '物理', '地理', '历史', '生物']
console.log(newLenth); // 9 ，unshift()方法返回值和push()方法一样是数组新长度

// 删除元素
let lastCourse = courseArr.pop(); // 从数组中删除最后一个元素
console.log(lastCourse); // 生物 ，pop()方法返回删除的元素
let firstCourse = courseArr.shift(); // 从数组首部删除一个元素
console.log(courseArr); // ['政治', '数学', '英语', '语文', '物理', '地理', '历史']
console.log(firstCourse); // 化学 ，shift()方法返回值和pop()方法一样是被删除的元素
```



### Object

JavaScript中将一切看作为对象（Object），一个对象由花（大）括号`{ }`括起来，由属性名和对应的属性值组成，属性值可以是任意类型，比如数值、字符串、布尔值、数组，甚至是对象。各组属性由`,`分隔，每组属性中的属性名和属性值由`:`分隔。

```js
let car = {name: "Benz", color: "white", price: 1000000};
console.log(car); // {name: 'Benz', color: 'white', price: 1000000}
console.log(car.name); // Benz

let person = { name: "Jack", age: 18 };
console.log(person.name); // Benz

let book = { name: "Python", author: { name: "Mike", birth: "1990-01-01" } };
console.log(book.author.name); //Mike
```

对对象的属性进行访问通过`.属性名`，如上例中的`car.name`、`book.author.name`。

对象除了包含如上所述的数据信息外，还可以包含函数等内容。具体可见后面的章节：[对象](#对象)。



## 运算符

### 算术运算符

| 运算符 |    说明    |       示例        |
| :----: | :--------: | :---------------: |
|  `+`   |     加     |        4+2        |
|  `-`   |     减     |        9-3        |
|  `*`   |     乘     |        2*5        |
|  `/`   |     除     |        5/3        |
|  `%`   | 模（取余） |      110%13       |
|  `**`  |     幂     | 5\*\*2，等价5\*5  |
|  `++`  |   自增1    |        a++        |
|  `--`  |   自减1    |        a--        |
|  `+=`  |            | a+=10，等价a=a+10 |
|  `-=`  |            | a-=10，等价a=a-10 |
|  `*=`  |            | a\*=2，等价a=a\*2 |
|  `/=`  |            |  a/=5，等价a=a/5  |
|  `%=`  |            |  a%=5，等价a=a%5  |

**JavaScript的算术运算中会进行正确的计算，即不会像C/C++、Java那样对两个整数的除法运算进行取整。**

```js
console.log(3/5); // 0.6
console.log(3.64 % 2.5); //1.1400000000000001
```



`+`和`+=`还可以用于字符串拼接，如：

```js
let str1="hello ", str2="world !";

let str3=str1+", Jack.";
console.log(str3);  //hello , Jack.

str1+=str2;
console.log(str1); //hello world !
```



### 比较运算符

| 运算符 |           说明           |  示例   |
| :----: | :----------------------: | :-----: |
| `===`  |   等于（是否完全一样）   | a === b |
| `!==`  | 不等于（是否不完全一样） | a !== b |
|  `<`   |           小于           |  a < b  |
|  `>`   |           大于           |  a > b  |
|  `<=`  |         小于等于         | a <= b  |
|  `>=`  |         大于等于         | a >= b  |

**注意：JavaScript的等于运算符使用的三个等号`===`，而不是C/C++、Java的两个等号`==`。**



### 逻辑运算符

| 运算符 |  说明  |   示例   |
| :----: | :----: | :------: |
|  `&&`  | 逻辑与 |  a && b  |
|  `||`  | 逻辑或 | a \|\| b |
|  `!`   | 逻辑非 |   ! a    |

+ 逻辑与：允许你把两个或多个表达式连在一起，这样所有的表达式都必须单独求值为 `true`，整个表达式才会返回 `true`。
+ 逻辑或：允许你把两个或多个表达式连在一起，其中有一个或多个表达式单独求值为 `true`，整个表达式就会返回 `true`。



### 三元（条件）运算符

```
表达式 ? 表达式1 : 表达式2 ;
```

三元或条件运算符是一个很简单的语法，其用于测试一个条件，如果条件为 `true` 则返回一个值或表达式（表达式1），否则（`false`）返回另外一个（表达式2）。



## 流程控制语句

### 条件语句

```
// 形式一
if (条件) {
	满足条件执行
}

// 形式二
if (条件) {
	满足条件执行
} else {
	不满足条件执行
}

// 形式三
if (条件1) {
	满足条件1执行
} else if (条件2) {
	不满足条件1，但满足条件2执行
} else {
	不满足条件1，且不满足条件2执行
}

// 形式四
if (条件1) {
	if (条件2) {
		满足条件1，且满足条件2执行
	} else if (条件3) {
		满足条件1，不满足条件2，但满足条件3执行
	} else {
		满足条件1，不满足条件2，且不满足条件3执行
	}
} else if (条件4) {
	不满足条件1，但满足条件4执行
} else if (条件5) {
	不满足条件1，不满足条件4，但满足条件5执行
} else {
	if (条件6) {
		不满足条件1，不满足条件4，不满足条件5，但满足条件6执行
	} else {
		不满足条件1，不满足条件4，不满足条件5，且不满足条件6执行
	}
}
```

上述伪代码中，形式一、形式二、形式三是条件语句基本使用形式，形式四则是`if...else`语句的嵌套使用形式，一般不建议嵌套过多。

说明：***任何不是 `false`、`undefined`、`null`、`0`、`NaN`、或空字符串（`''`）的值在作为条件语句进行测试时实际返回 `true`。***



### 多分支（“开关”）语句

```
switch (表达式) {
  case 值1:
    表达式值为值1时执行
    break;

  case 值2:
    表达式值为值2时执行
    break;

  // 包含尽可能多的情况

  default:
    当表达式值不在预期中执行
    break;
}
```

`switch`语句以单个表达式或值作为输入，然后查看多个选项（设定值），直到找到与该值相匹配的选项，执行与之相关的代码。

关键字 `case`，后跟一个选项的表达式或值，后面跟一个冒号。

一个 `break` 语句，分号结尾。如果先前的选择与表达式或值匹配，则浏览器在此停止执行`switch`语句代码块，并执行 `switch` 语句之后的代码。

`default` 部分不是必须的——如果表达式不可能存在未知值，则可以安全地省略它。然而，如果有这样的可能，你需要包含它来处理未知的情况。





### 循环语句

一段循环通常需要一个或多个条件：

- **一个开始条件，**它被初始化为一个特定的值 - 这是循环的起点。
- **一个结束条件，**这是循环停止的标准 - 通常计数器达到一定值。
- **一个迭代器，**这通常在每个连续循环上递增少量的计数器，直到达到退出条件。



#### for循环

```
for (初始化; 循环结束条件; 步长) {
  循环执行
}
```

关键字`for`后面的`()`括号内，有三个部分，以分号`;`分隔：

1.一个**初始化器** - 这通常是一个设置为一个数字的变量，它被递增来计算循环运行的次数。它也有时被称为**计数变量**。
2.一个**退出条件** - 如前面提到的，这个定义循环何时停止循环。这通常是一个表现为比较运算符的表达式，用于查看退出条件是否已满足的测试。
3.一个**步长（迭代器）** - 这总是被判断（或运行），每个循环已经通过一个完整的迭代消失时间。它通常用于增加（或在某些情况下递减）计数器变量，使其更接近退出条件值。



#### while语句

```
初始化
while (循环结束条件) {
  循环执行
  步长
}
```

除了在循环之前设置初始化器变量，并且在运行代码之后，循环中包含步长（迭代器），而不是这两个项目被包含在括号中。



#### `do...while`循环

```
初始化
do {
  循环执行
  步长
} while (循环结束条件)
```

在`do ... while`循环中，花括号中的代码总是在检查之前运行一次，以查看是否应该再次执行（在`while `和`for`循环中，检查首先出现，因此代码可能永远不会执行）。



#### `for...of`循环

```js
// for...of循环
for (let i of [1, 2, 3, 4, 5]) {
  console.log(i);
}

// 等价
const arr = [1, 2, 3, 4, 5];
for (let i of arr) {
  console.log(i);
}
```

在JavaScript中数组由`[ ]`中的元素组成，如`[1, 2, 3, 4, 5]`、`["hello","world","good","today"]`。

`for...of`循环提供了一种获取数组中的每一个元素的方法，也即遍历数组元素。



#### `break`语句

如果要在所有循环（迭代）完成之前退出（结束）循环，可以使用 `break` 语句。当执行到`break`语句时，将立即退出循环。

```js
for (let i = 0 ; i < 10 ; i++) {
	if (i === 5){
		break;
	}
	......
}
```



#### `continue`语句

`continue`语句不是完全跳出循环，而是**跳过当前循环去执行下一个循环**，当前循环中位于`continue`语句之后的语句将不执行。

```js
for (let i = 0 ; i < 10 ; i++) {
	if (i % 2 === 0){
		continue;
	}
	......
}
```



## 迭代



## 函数

### 函数定义（声明）

```js
function myFunction(){
	console.log("自定义了一个函数！")
}

myFunction();
printInfo("李伟", 20, "北京大学");
printInfoByDefault("李伟", 22);

function printInfo(name, age, school) {
    console.log("你的名字是：", name);
    console.log("你的年龄是：", age);
    console.log("你的学校是：", school);
}

function printInfoByDefault(name, age = 18, school = "未知") {
    console.log("你的名字是：", name);
    console.log("你的年龄是：", age);
    console.log("你的学校是：", school);
}
```

定义函数使用`function`关键字，函数名自定义，小括号`()`中没有形参表示无参函数，函数体被大括号`{}`括起来。在调用函数希望传递参数给函数，可以在小括号`()`内写上参数名（形参），这样函数就是有参数函数。

使用`function`关键字、函数名、`()`、`{}`这种创建函数的形式，也被称为函数声明。**函数声明总是被提升的（也叫函数提升），这样就能在函数定义之前调用该函数。**

在编写一个函数时，希望支持可选参数，你可以在参数名称后添加 `=`，然后再添加默认值来指定对应参数的默认值。当没有传递实际的参数时，将使用默认值。如上述代码中的`printInfoByDefault("李伟", 22);`，这里需要注意的是省略实参只能从最后的参数开始，比如像`printInfoByDefault("李伟", , "清华大学");`将报语法错误，而`printInfoByDefault("李伟");`则没有问题。



### 匿名函数

```js
// 匿名函数声明
(function () {
  console.log("匿名函数");
});

// 匿名函数直接运行（调用）
(function () {
  console.log("运行了匿名函数");
})();

// 匿名函数作为函数参数传递
funcWithFuncAgr(name, function(num1, num2){
    console.log("两数之和为：", num1+num2);
});
```

匿名函数顾名思义没有函数名的函数。匿名函数和普通函数一样可以有参数。

由于匿名函数没有函数名，不能通过函数名显式地进行调用，所以当一个函数希望接收另一个函数作为参数时，会经常看到匿名函数。在这种情况下，匿名函数通常作为实际的函数参数进行传递。

**这种创建函数的形式也称为函数表达式。与函数声明不同，函数表达式不会被提升。**



### 箭头函数

匿名函数的另一种等价形式是箭头函数。

```js
// 箭头函数声明
() => {
  console.log("箭头函数");
};

// 直接运行箭头函数
(() => {
  console.log("箭头函数");
})();

// 箭头函数作为函数参数传递
funcWithFuncAgr(name, (num1, num2) => {
    console.log("两数之和为：", num1+num2);
});

// 若箭头函数只有一个参数，可简洁编写
funcWithFuncAgr(name, num1 => {
    console.log("数字为：", num1);
});

//  若箭头函数只包含一条语句，可简洁编写
funcWithFuncAgr(name, num1 => 
    console.log("数字为：", num1).
);

// 若箭头函数内仅仅只是一条return语句，可省略return关键字
funcWithFuncAgr(name, num1 => 2*num1);
```

建议使用箭头函数，因为它们可以使代码更简短、更易读。



### 函数返回值

返回值就是指函数执行完毕后返回的值。一般来说，返回值用于函数作为计算的中间步骤。

要从自定义函数返回值，你需要使用 `return` 关键字。

```js
function doubleNum (num) {
	return 2*num;
}
```



### 函数作用域与冲突

当创建一个函数时，函数内定义的变量和其他东西都在它们自己的、单独的作用域内，意味着它们被锁在自己独立的隔间中，不能被函数外的代码访问。

所有函数的最外层被称为全局作用域。在全局作用域内定义的值可以在任意地方访问。

有时不希望变量可以在代码中的任何地方被访问到——从其他地方调用的外部脚本可能会开始干扰自己的代码并导致问题，因为它们可能与代码的其它部分使用了相同的变量名称，造成冲突。

**将部分代码锁定在函数中避免了这样的问题，并被认为是最佳实践。**



## 对象

对象是一个包含相关数据和方法的集合（通常由一些变量和函数组成，称之为对象里面的属性和方法）。

### 对象声明（表示）

一个对象变量可以初始化为`空`：

```js
let obj1 = {};
console.log(typeof obj1); // object
console.log(obj1); // {}
```

一个包含数据和方法的对象：

```js
let person = {
  name: ["Bob", "Smith"],
  age: 32,
  bio: function () {
    console.log(`${this.name[0]} ${this.name[1]} 现在 ${this.age} 岁了。`);
  },
  introduceSelf: function () {
    console.log(`你好！我是 ${this.name[0]}。`);
  },
};

// 访问（调用）对象变量的方法（函数）
person.bio();
person.introduceSelf();
```

可见，一个对象由许多的成员组成，每一个成员都拥有一个名字（如 `name`、`age`）和一个值（如 `['Bob', 'Smith']`、`32`）。每一组名字与值必须由逗号分隔开，并且名字和值之间由冒号分隔。

对象成员的值可以是任意的，数据项被称为对象的**属性**，允许对象对该数据进行某些操作的函数称为对象的**方法**。

当对象的成员是函数时，语法会更简单。我们可以写 `bio()` 来代替 `bio: function()`。

```js
let person = {
  name: ["Bob", "Smith"],
  age: 32,
  bio() {
    console.log(`${this.name[0]} ${this.name[1]} 现在 ${this.age} 岁了。`);
  },
  introduceSelf() {
    console.log(`你好！我是 ${this.name[0]}。`);
  },
};
```



### 对象成员访问与设置

使用**点表示法**（dot notation）来访问对象的属性和方法。对象的名字表现为一个**命名空间**（namespace）。当想访问对象内部的属性或方法时，命名空间必须写在第一位。然后输入一个点`.`，紧接着是想要访问的目标——可以是简单属性的名字，或者是数组属性的一个子元素，又或者是对象的方法调用。

```js
person.age;
person.bio();
```

另外一种访问对象属性的方式是使用**括号表示法**（bracket notation），如：

```js
person["age"];
```

点表示法通常优于括号表示法，因为它更简洁且更易于阅读。然而，**在某些情况下必须使用括号。例如，如果对象属性名称保存在变量中，则不能使用点表示法访问该值，但可以使用括号表示法访问该值。**如：

```js
const person = {
  name: ["Bob", "Smith"],
  age: 32,
};

function logProperty(propertyName) {
  console.log(person[propertyName]);
}

logProperty("name"); // ["Bob", "Smith"]
logProperty("age"); // 32
```

可以通过声明**设置**（更新）对象成员的值（使用点表示法或括号表示法），甚至可以创建新的成员。

```js
let book = {
	name: "JavaScript",
    price: 48.8,
    printInfo(){
        console.log(`Book name is ${this.name}`);
    },
}

book.name = "New JavaScript";
book["price"] = 66.2
book.author = "John";
book.printInfo = function(){
    console.log(`Book name is ${this.name}, and price is ${this.price}.`);
}

console.log(book); // {name: 'New JavaScript', price: 66.2, printInfo: ƒ, author: 'John'}
```

**括号表示法**一个有用的地方是它不仅可以动态的去设置对象成员的值，还**可以动态的去设置成员的名字**。

```js
let propertyName = "publication";
let propertyValue = "2022-06-08";

book[propertyName] = propertyValue;

console.log(book); // {name: 'New JavaScript', price: 66.2, printInfo: ƒ, author: 'John', publication: '2022-06-08'}
```

这是使用点表示法无法做到的，**点表示法只能接受字面量的成员的名字，不接受表示名称的变量**。



### this关键字

关键字 `this` 指向了当前代码运行时的对象。如：

```js
let book = {
	name: "JavaScript",
    price: 48.8,
    printInfo(){
        console.log(`Book name is ${this.name}`);
    },
}

book.printInfo(); // Book name is JavaScript

book.printInfo = function(){
    console.log(`Book name is ${this.name}, and price is ${this.price}.`);
}

book.printInfo(); // Book name is New JavaScript, and price is 66.2.
```



### 构造函数

希望有一种方法来定义对象的“特征”，即方法集和属性集，然后可以创建任意多个对象，只需更新不同属性的值。

一种朴素的方式是通过一个函数实现：

```js
function createBook(name, price) {
  let book = {};
  book.name = name;
  book.price = price;
  book.printInfo = function () {
    console.log(`Book name is ${this.name}, and price is ${this.price}.`);
  };
  return book;
}

let book1 = createBook("JavaScript", 66.2);
let book2 = createBook("Python", 48.8);
```

该方式通过一个函数去执行如下步骤：创建一个空对象，设置对象的值，返回对象。

另一种方式是通过**构造函数**实现：

```js
function Book(name, price) {
  this.name = name;
  this.price = price;
  this.printInfo = function () {
    console.log(`Book name is ${this.name}, and price is ${this.price}.`);
  };
}

let book3 = new Book("Java", 39.8);
let book4 = new Book("C++", 48.8);
```

构造函数只是使用 `new` 关键字调用的函数。当调用构造函数时，它将：创建一个新对象，将 `this` 绑定到新对象，以便可以在构造函数代码中引用 `this`，运行构造函数中的代码，返回新对象。

按照惯例，**构造函数以大写字母开头，并且以它们创建的对象类型命名**。









