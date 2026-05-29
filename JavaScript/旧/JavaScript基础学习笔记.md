# JavaScript基础学习

## JavaScript概述

JavaScript 是一门编程语言，可为网站添加交互功能（例如：游戏、动态样式、动画以及在按下按钮或收到表单数据时做出的响应等）。

JavaScript（缩写：JS）是一门完备的动态编程语言。当应用于HTML文档时，可为网站提供动态交互特性。由布兰登·艾克（Brendan Eich，Mozilla 项目、Mozilla 基金会和 Mozilla 公司的联合创始人）发明。

JavaScript 的应用场合极其广泛，简单到幻灯片、照片库、浮动布局和响应按钮点击，复杂到游戏、2D/3D 动画、大型数据库驱动程序等等。

JavaScript 相当简洁，却非常灵活。开发者们基于 JavaScript 核心编写了大量实用工具，可以使 开发工作事半功倍。其中包括：

+ 浏览器应用程序接口（API）——浏览器内置的 API 提供了丰富的功能，比如：动态创建 HTML 和设置 CSS 样式、从用户的摄像头采集处理视频流、生成 3D 图像与音频样本等等。
+ 第三方API——让开发者可以在自己的站点中整合其他内容提供者（Twitter、Facebook 等）提供的功能。
+ 第三方框架和库——用来快速构建网站和应用。

## JavaScript引入到HTML页面

将JavaScript引入到HTML中，需要使用`<script>`元素（标签）。

### 直接在HTML文档中编写JS代码

如：

```html
<html>
    <head>...</head>
    <body>...</body>
    <style>...</style>
    <script language="JavaScript">
            JavaScript code...
    </script>
</html>
```



### 将编写好的js文件引入到HTML中

对常用或复用性高的JavaScript代码，可以将JavaScript代码编写好后保存在`.js`文件中，然后在HTML文档中引入。此方法需要设置`<script>`元素的属性`src`。

如：

```html
<html>
    <head>...</head>
    <body>...</body>
    <style>...</style>
    <script type="text/javascript" src="filePath/fileName.js"></script>
    <script language="JavaScript">JavaScript code...</script>
</html>
```



***注意：我们将`<script>`放在 HTML 文件的底部附近的原因是浏览器会按照代码在文件中的顺序加载 HTML。如果先加载的 JavaScript 期望修改其下方的 HTML，那么它可能由于 HTML 尚未被加载而失效。因此，将 JavaScript 代码放在 HTML 页面的底部附近通常是最好的策略。***

## JavaScript快速入门

### 注释

**Javascript 注释**的语法和 C++ 或许多其他语言类似：

```
// 单行注释

/* 这是一个更长的，
   多行注释
*/

/* 然而，你不能，/* 嵌套注释 */ 语法错误 */
```



### 变量（Variable）

变量是存储值的容器。要声明一个变量，先输入关键字`let`或`var`，然后输入合适的名称，如`let myVariable;`。

关于`let`和`var`的区别：

1. `var`用于声明一个**函数作用域或全局作用域**的变量，并且可以选择将其初始化为一个值。
2. `let`用于声明可重新赋值的**块级作用域局部变量**，并且可以选择将其初始化为一个值。

变量命名的规则：一个 JavaScript 标识符必须以字母、下划线（_）或者美元符号（$）开头；后续的字符也可以是数字（0-9）。因为 JavaScript 语言是区分大小写的，所以字母可以是从“A”到“Z”的大写字母和从“a”到“z”的小写字母。

JavaScript是一种有着动态类型的动态语言。JavaScript中的变量与人恶化特定值类型没有任何关联，任何变量都可以被赋予（和重新赋予）各种类型的值。

如

```javascript
let foo = 42; // foo 现在是一个数值
foo = "bar"; // foo 现在是一个字符串
foo = true; // foo 现在是一个布尔值
```

JavaScript也是一个弱类型语言，这意味着当操作涉及不匹配的类型时，它允许隐式类型转换，而不是抛出类型错误。

```javascript
const foo = 42; // foo 现在是一个数值
const result = foo + "1"; // JavaScript 将 foo 强制转换为字符串，因此可以将其与另一个操作数连接起来
console.log(result); // 421
```

隐式强制转换是非常方便的，但当转换发生在预期之外的地方，或发生在预期的另一个方向（例如，字符串转换为数值，而不是数值转换为字符串）时，就会产生一些微妙的错误。对于 symbol和 BigInt，JavaScript 有意禁止了某些隐式类型转换。

如果声明了一个变量却没有对其赋值，那么这个变量的类型就是 `undefined`。

### JavaScript数据类型和数据结构

JavaScript的数据类型结构：

+ `Number`（数字）
+ `String`（字符串）
+ `Boolean`（布尔）
+ `Symbol`（符号）（ES2015新增）
+ `Object`（对象）
  + `Function`（函数）
  + `Array`（数组）
  + `Date`（日期）
  + `RegExp`（正则表达式）
+ `null`（空）
+ `undefined`（未定义）

#### 数字（Number）

根据语言规范，JavaScript 采用“遵循 IEEE 754 标准的双精度 64 位格式”（"double-precision 64-bit format IEEE 754 values"）表示数字。——在 JavaScript（除了`BigInt`）当中，**并不存在整数/整型 (Integer)。**因此在处理如下的场景时候，你一定要小心：

```javascript
console.log(3 / 2);             // 1.5,not 1
console.log(Math.floor(3 / 2)); // 1
```

**一个看上去是整数的东西，其实都是浮点数。**

JavaScript 支持标准的算术运算符，包括加法、减法、取模（或取余）等等。还有一个之前没有提及的内置对象 `Math`（数学对象），用以处理更多的高级数学函数和常数：

```javascript
Math.sin(3.5);
var circumference = 2 * Math.PI * r;
```



可以使用内置函数`parseInt()`将字符串转换为整型。该函数的第二个可选参数表示字符串所表示数字的基（进制）：

```javascript
parseInt("123", 10); // 123
parseInt("010", 10); // 10
parseInt("11", 2); // 3
```

JavaScript 还有一个类似的内置函数 `parseFloat()`，用以解析浮点数字符串，与`parseInt()`不同的地方是，`parseFloat()` 只应用于解析十进制数字。

一元运算符 + 也可以把数字字符串转换成数值：

```javascript
+"42"; // 42
+"010"; // 10
+"0x10"; // 16
```

如果给定的字符串不存在数值形式，函数会返回一个特殊的值 `NaN`（Not a Number 的缩写）：

```javascript
parseInt("hello", 10); // NaN
```

*注：`parseInt()`和 `parseFloat()`函数会尝试逐个解析字符串中的字符，直到遇上一个无法被解析成数字的字符，然后返回该字符前所有数字字符组成的数字。但是运算符 "+"对字符串的转换方式与之不同，只要字符串含有无法被解析成数字的字符，该字符串就将被转换成 `NaN`。可分别使用这两种方法解析“10.2abc”这一字符串，并比较得到的结果，来理解这两种方法的区别。*

要小心 NaN：如果把 `NaN` 作为参数进行任何数学运算，结果也会是 `NaN`。可以使用内置函数`isNaN()`来判断一个变量是否为`NaN`：

```javascript
isNaN(NaN); // true
```

JavaScript 还有两个特殊值：`Infinity`（正无穷）和 `-Infinity`（负无穷）：

```javascript
1 / 0; //  Infinity
-1 / 0; // -Infinity
```

可以使用内置函数 `isFinite()`来判断一个变量是否是一个有穷数，如果类型为`Infinity`, `-Infinity` 或 `NaN 则返回 false`。

JavaScript 的算术操作符包括 `+`、`-`、`*`、`/` 和 `%`——求余（与模运算相同）。赋值使用 `=` 运算符，此外还有一些复合运算符，如 `+=` 和 `-=`，它们等价于 `x = x operator y`。

可以使用 `++` 和 `--` 分别实现变量的自增和自减。两者都可以作为前缀或后缀操作符使用。

#### 字符串（String）

JavaScript 中的字符串是一串**Unicode 字符**序列。这对于那些需要和多语种网页打交道的开发者来说是个好消息。更准确地说，它们是一串 UTF-16 编码单元的序列，每一个编码单元由一个 16 位二进制数表示。每一个 Unicode 字符由一个或两个编码单元来表示。

通过访问字符串的`length`（编码单元的个数）属性，可以得到它的长度。

```javascript
"hello".length; // 5
```

字符串也提供方法能让你操作字符串和获取字符串的信息。

```js
"hello".charAt(0); // "h"
"hello, world".replace("world", "mars"); // "hello, mars"
"hello".toUpperCase(); // "HELLO"
```

`+`操作符可以用来连接字符串：

```js
"hello" + " world"; // hello world
```

如果你用一个字符串加上一个数字（或其他值），那么操作数都会被首先转换为字符串。

#### 布尔（Boolean）

JavaScript 包含布尔类型，这个类型的变量有两个可能的值，分别是 `true` 和 `false`（两者都是关键字）。根据具体需要，JavaScript 按照如下规则将变量转换成布尔类型：

1. `false`、`0`、空字符串（`""`）、`NaN`、`null`和`undefined`被转换为`false`
2. 所有其他值被转换为`true`

也可以使用 `Boolean()` 函数进行显式转换：

```js
Boolean(""); // false
Boolean(234); // true
```

JavaScript 支持包括 `&&`（逻辑与）、`||` （逻辑或）和`!`（逻辑非）在内的一些逻辑运算符。

JavaScript 中的比较操作使用 `<`、`>`、`<=` 和 `>=`，这些运算符对于数字和字符串都通用。相等的比较稍微复杂一些。由两个“`=`（等号）”组成的相等运算符有类型自适应的功能，具体例子如下：

```js
123 == "123"; // true
1 == true; // true
```

**如果在比较前不需要自动类型转换，应该使用由三个“`=`（等号）”组成的相等运算符**：

```js
1 === true; //false
123 === "123"; // false
```

JavaScript 还支持 `!=` 和 `!==` 两种不等运算符，具体区别与两种相等运算符的区别类似。

#### 符号（Symbol）

`symbol`是**唯一并且不可变**的原始值并且可以用来作为对象属性的键。在某些程序语言当中，Symbol 也被称作“原子（atom）类型”。symbol 的目的是去创建一个唯一属性键，保证不会与其他代码中的键产生冲突。

#### 对象（Object）

在 JavaScript 中，对象是唯一可变的值。事实上，函数也是具有额外可调用能力的对象。

创建一个空对象：

```js
var obj = new Object(); 
//等价的方式
var obj = {};
```

这两种方法在语义上是相同的。第二种更方便的方法叫作“对象字面量（object literal）”法。这种也是 JSON 格式的核心语法，一般我们优先选择第二种方法。

在 JavaScript 中，对象可以被看作是一组属性的集合。用对象字面量语法来定义一个对象时，会自动初始化一组有限的属性；然后，这些属性还可以被添加和移除。对象属性等价于键值对（而不是键值对：现在，ES 2015 的映射表（Map），比对象更接近键值对）。属性键要么是字符串类型，要么是symbol。属性值可以是任何类型的值，包括其他对象，从而可以构建复杂的数据结构。

“对象字面量”也可以用来在对象实例中定义一个对象：

```js
var obj = {
  name: "Carrot",
  _for: "Max", //'for' 是保留字之一，使用'_for'代替
  details: {
    color: "orange",
    size: 12,
  },
};
```

对象的属性可以通过链式（chain）表示方法进行访问：

```js
obj.details.color; // orange
obj["details"]["size"]; // 12
```

下面的例子创建了一个对象原型，**`Person`**，和这个原型的实例，**`You`**。

```js
function Person(name, age) {
  this.name = name;
  this.age = age;
}

// 定义一个对象
var You = new Person("You", 24);
// 我们创建了一个新的 Person，名称是 "You"
// ("You" 是第一个参数，24 是第二个参数..)
```

完成创建后，对象属性可以通过如下两种方式进行赋值和访问：

```js
//方式一
// 点表示法 (dot notation)
obj.name = "Simon";
var name = obj.name;

//方式二
// 括号表示法 (bracket notation)
obj["name"] = "Simon";
var name = obj["name"];
// can use a variable to define a key
var user = prompt("what is your key?");
obj[user] = prompt("what is its value?");
```

这两种方法在语义上也是相同的。第二种方法的优点在于属性的名称被看作一个字符串，这就意味着它可以在运行时被计算，缺点在于这样的代码有可能无法在后期被解释器优化。它也可以被用来访问某些以预留关键字作为名称的属性的值：

```js
obj.for = "Simon"; // 语法错误，因为 for 是一个预留关键字
obj["for"] = "Simon"; // 工作正常
```



有两种对象属性的类型：数据属性和访问器属性。每个属性都有对应的*特性*（attribute）。JavaScript 引擎可在内部访问每个属性，但是你可以通过 `Object.defineProperty()`设置它们，或通过`Object.getOwnPropertyDescriptor()` 读取它们。

+ 数据属性

  数据属性将键与值相关联。它可以通过以下属性来描述：

  + `value`

    通过属性访问器获取值。可以是任意的JavaScript值。

  + `writeable`

    一个布尔值，表示是否可以通过赋值来改变属性。

  + `enumerable`

    一个布尔值，表示是否可以通过`for...in`循环来枚举属性。

  + `configurable`

    一个布尔值，表示该属性是否可以删除，是否可以更改为访问器属性，并可以更改其特性。

+ 访问器属性

  将键与两个访问器函数（`get`和`set`）相关联，以获取或者存储值。一个访问器属性有着以下特性：

  + `get`

    该函数使用一个空的参数列表，以便有权对值执行访问时，获取属性值。

  + `set`

    使用包含分配值的参数调用的函数。每当尝试更改指定属性时执行。可能是`undefined`。

  + `enumerable`

    一个布尔值，表示是否可以通过`for...in`循环来枚举属性。

  + `configurable`

    一个布尔值，表示该属性是否可以删除，是否可以更改为访问器属性，并可以更改其特性。

##### 函数（Function）

最简单的函数就像下面这个这么简单：

```js
function add(x, y) {
  var total = x + y;
  return total;
}
```

这个例子包括你需要了解的关于基本函数的所有部分。一个 JavaScript 函数可以包含 0 个或多个已命名的变量。函数体中的表达式数量也没有限制。你可以声明函数自己的局部变量。`return` 语句在返回一个值并结束函数。如果没有使用 `return` 语句，或者一个没有值的 `return` 语句，JavaScript 会返回 `undefined`。

已命名的参数更像是一个指示而没有其他作用。如果调用函数时没有提供足够的参数，缺少的参数会被 `undefined` 替代。

***需要注意的是 JavaScript 函数是它们本身的对象——就和 JavaScript 其他一切一样——你可以给它们添加属性或者更改它们的属性，这与前面的对象部分一样。***

##### 数组（Array）

JavaScript 中的数组是一种特殊的对象。它的工作原理与普通对象类似（以数字为属性名，但只能通过`[]` 来访问），但数组还有一个特殊的属性——`length`（长度）属性。这个属性的值通常比数组最大索引大 1。

创建数组的传统方法是：

```js
var a = new Array();
a[0] = "dog";
a[1] = "cat";
a[2] = "hen";
a.length; // 3
```

使用数组字面量（array literal）法更加方便：

```js
var a = ["dog", "cat", "hen"];
a.length; // 3
```

注意，`Array.length` 并不总是等于数组中元素的个数，如下所示：

```js
var a = ["dog", "cat", "hen"];
a[100] = "fox";
a.length; // 101
```

如果试图访问一个不存在的数组索引，会得到 `undefined`。

可以通过如下方式遍历一个数组：

```js
for (var i = 0; i < a.length; i++) {
  // Do something with a[i]
}
```

ES2015 引入了更加简洁的 `for`...`of`循环，可以用它来遍历可迭代对象，例如数组：

```js
for (const currentValue of a) {
  // Do something with currentValue
}
```

遍历数组的另一种方法是使用 `for...in`循环，然而这并不是遍历数组元素而是数组的索引。注意，如果哪个家伙直接向 `Array.prototype` 添加了新的属性，使用这样的循环这些属性也同样会被遍历。所以并不推荐使用这种方法遍历数组：

```js
for (var i in a) {
  // 操作 a[i]
}
```

ECMAScript 5 增加了另一个遍历数组的方法，`forEach()`：

```js
["dog", "cat", "hen"].forEach(function (currentValue, index, array) {
  // 操作 currentValue 或者 array[index]
});
```

如果想在数组后追加元素，只需要：

```js
a.push(item);
```



##### 日期（Date）

当表示日期时，最好的选择是使用在 JavaScript 内置的 `Date`工具类。

#### 空（Null）

Null类型只有一个值：`null`。

`null` 值特指为不存在任何对象值。它是 JavaScript 的原始值之一，且在布尔运算中被视为假值。

值 `null` 被写作字面量：`null`。不像 `undefined`，`null` 不是全局对象的属性。相反，`null` 是表示缺少的标识，指示变量未指向任何对象。在 API 中，`null` 常在预期的值应是一个对象，但又没有关联的对象的地方使用。

```js
// foo 不存在。它从未被定义或初始化：
foo; //ReferenceError: foo is not defined

// 已知 foo 现在已经存在，但它没有类型和值：
const foo = null;
foo; //null
```

当检查值是否为 `null` 或 `undefined` 时，请注意相等（`==`）与全等（`===`）运算符的区别，前者会执行类型转换：

```js
typeof null; // "object"（因历史原因而不是 "null"）
typeof undefined; // "undefined"
null === undefined; // false
null == undefined; // true
null === null; // true
null == null; // true
!null; // true
Number.isNaN(1 + null); // false
Number.isNaN(1 + undefined); // true
```

#### 未定义（Undefined）

Undefined 类型只有一个值：`undefined`。

从概念上讲，`undefined` 表示*值*的缺失，`null` 表示*对象*的缺失（这也可以说明`typeof null === "object"`的原因）。当某些东西没有值时，该语言通常默认为 `undefined`：

+ 没有值（`return;`)的`return`语句，隐式返回`undefined`。
+ 访问不存在的对象属性（obj.iDontExist)，返回`undefined`。
+ 变量声明时没有初始化（`let x;`），隐式初始化为`undefined`。
+ 许多像`Array.prototype.find()`和`Map.prototype.get()`的方法，当没有找到元素时，返回`undefined`。

`null` 是一个关键字，但是 `undefined` 是一个普通的标识符，恰好是一个全局属性。在实践中，这两个差异很小，因为 `undefined` 不应该被重新定义或者遮蔽。

### 流程控制语句

#### 条件语句

条件语句是一种代码结构，用来测试表达式的真假，并根据测试结果运行不同的代码。一个常用的条件语句是 `if ... else`。下面是一个示例：

```js
let iceCream = "chocolate";
if (iceCream === "chocolate") {
  alert("我最喜欢巧克力冰淇淋了。");
} else {
  alert("但是巧克力才是我的最爱呀……");
}
```

`if`和`else`可以嵌套使用：

```js
var name = "kittens";
if (name == "puppies") {
  name += "!";
} else if (name == "kittens") {
  name += "!!";
} else {
  name = "!" + name;
}
name == "kittens!!"; // true
```



#### 循环语句

JavaScript 支持 `while` 循环和 `do-while` 循环。前者适合常见的基本循环操作，如果需要循环体至少被执行一次则可以使用 `do-while`：

```js
while (true) {
  // 一个无限循环！
}

var input;
do {
  input = get_input();
} while (inputIsNotValid(input));
```

JavaScript 的 `for`循环与 C 和 Java 中的相同：使用时可以在一行代码中提供控制信息。

```js
for (var i = 0; i < 5; i++) {
  // 将会执行五次
}
```

JavaScript 也还包括其他两种重要的 for 循环： “`for...of`”和“`for...in`”：

```js
//遍历数组（遍历的是数组元素）
for (let value of array) {
  // do something with value
}

//遍历对象的属性，也可以用于遍历数组（遍历的是数组索引）
for (let property in object) {
  // do something with object property
}
```



#### 多分支语句

可以使用基于一个数字或字符串的 `switch` 语句：

```js
switch (action) {
  case "draw":
    drawIt();
    break;
  case "eat":
    eatIt();
    break;
  default:
    doNothing();
}
```

如果你不使用 `break` 语句，JavaScript 解释器将会执行之后 `case` 中的代码。除非是为了调试，一般你并不需要这个特性，所以大多数时候不要忘了加上 `break`。

`default` 语句是可选的。`switch` 和 `case` 都可以使用需要运算才能得到结果的表达式；在 `switch` 的表达式和 `case` 的表达式是使用 `===` 严格相等运算符进行比较的：

```js
switch (1 + 3) {
  case 2 + 2:
    yay();
    break;
  default:
    neverhappens();
}
```

