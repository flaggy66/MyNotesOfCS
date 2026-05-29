# JavaScript编程基础

## JavaScript介绍

**JavaScript**（**JS**）是一种具有**函数优先**特性的轻量级、**解释型**或者说即时编译型的编程语言。虽然作为 Web 页面中的脚本语言被人所熟知，但是它**也被用到了很多非浏览器环境中**，例如 Node.js、Apache CouchDB、Adobe Acrobat等。进一步说，JavaScript 是一种**基于原型、多范式、单线程的动态语言**，并且**支持面向对象、命令式和声明式（如函数式编程）风格**。

JavaScript 是一门跨平台、面向对象的脚本语言，它能使网页可交互（例如拥有复杂的动画，可点击的按钮，通俗的菜单等）。另外还有高级的服务端 Javascript 版本，例如 Node.js，它可以让你在网页上添加更多功能，不仅仅是下载文件（例如在多台电脑之间的协同合作）。在宿主环境（例如 web 浏览器）中，JavaScript 能够通过其所连接的环境提供的编程接口进行控制。

JavaScript 的动态特性包括运行时对象的构造、变量参数列表、函数变量、动态脚本创建（通过 `eval`）、对象内枚举（通过 `for...in`和 `Object` 工具方法）和源代码恢复（JavaScript 函数会存储其源代码文本，可以使用 `toString()` 进行检索）。

JavaScript 相当简洁，却非常灵活。开发者们基于 JavaScript 核心编写了大量实用工具，可以使 开发工作事半功倍。其中包括：

+ 浏览器应用程序接口（API）——浏览器内置的 API 提供了丰富的功能，比如：动态创建 HTML 和设置 CSS 样式、从用户的摄像头采集处理视频流、生成 3D 图像与音频样本等等。
+ 第三方API——让开发者可以在自己的站点中整合其他内容提供者（Twitter、Facebook 等）提供的功能。
+ 第三方框架和库——用来快速构建网站和应用。

JavaScript 内置了一些对象的标准库，比如数组（`Array`），日期（`Date`），数学（`Math`）和一套核心语句，包括运算符、流程控制符以及声明方式等。JavaScript 的核心部分可以通过添加对象来扩展语言以适应不同用途；例如：

- 客户端的 JavaScript 通过提供对象，控制浏览器及其文档对象模型（DOM），来扩展语言核心。例如：客户端的拓展代码允许应用程序将元素放在某个 HTML 表单中，并且支持响应用户事件，比如鼠标点击、表单提交和页面导航。
- 服务端的 JavaScript 则通过提供有关在服务器上运行 JavaScript 的对象来可扩展语言核心。例如：服务端版本直接支持应用和数据库通信，提供应用不同调用间的信息连续性，或者在服务器上执行文件操作。

这意味着，**在浏览器中，JavaScript 可以改变网页（DOM）的外观与样式**。同样地，**在服务器上，Node.js 中的 JavaScript 可以对浏览器上编写的代码发出的客户端请求做出响应**。

### JavaScript和Java的区别

JavaScript 和 Java 有一些共性但是在另一些方面有着根本性区别。JavaScript 语言类似 Java 但是并没有 Java 的静态类型和强类型检查特性。JavaScript 遵循了 Java 的表达式语法，命名规范以及基础流程控制，这也是 JavaScript 从 LiveScript 更名的原因。

与 Java 通过声明的方式构建类的编译时系统不同，JavaScript 采用基于少量的数据类型如数字、布尔、字符串值的运行时系统。JavaScript 拥有基于原型的对象模型提供的动态继承；也就是说，独立对象的继承是可以改变的。JavaScript 支持匿名函数。函数也可以作为对象的属性被当做宽松的类型方式执行。

与 Java 相比，Javascript 是一门形式自由的语言。你不必声明所有的变量，类和方法。你不必关心方法是否是公有、私有或者受保护的，也不需要实现接口。无需显式指定变量、参数、方法返回值的数据类型。

Java 是基于类的编程语言，设计的初衷就是为了确保快速执行和类型安全。类型安全，举个例子，你不能将一个 Java 整数变量转化为一个对象引用，或者由 Java 字节码访问专有存储器。Java 基于类的模型，意味着程序包含专有的类及其方法。Java 的类继承和强类型要求紧耦合的对象层级结构。这些要求使得 Java 编程比 JavaScript 要复杂的多。

相比之下，JavaScript 传承了 HyperTalk 和 dBASE 语句精简、动态类型等精髓，这些脚本语言为更多开发者提供了一种语法简单、内置功能强大以及用最小需求创建对象的编程工具。

| JavaScript                                                   | Java                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 面向对象。不区分对象类型。通过原型机制继承，任何对象的属性和方法均可以被动态添加。 | 基于类系统。分为类和实例，通过类层级的定义实现基础。不能动态增加对象或类的属性或方法。 |
| 变量类型不需要提前声明（动态类型）。                         | 变量必须提前声明（静态类型）。                               |
| 不能自动写入硬盘。                                           | 可以直接写入硬盘。                                           |

### 使用JavaScript

开始使用 JavaScript 很容易，你只需要一个现代 Web 浏览器。通过浏览器内置的Web**开发人员工具**中的Web**控制台**就可以使用JavaScript。

Web控制台不仅可以展示当前已加载页面的信息，还包含一个可以在当前页面执行JavaScript表达式的**命令行**。

#### 单行模式

控制台的工作方式与 eval 完全相同：返回最后输入的表达式。为了简单起见，可以想象每次输入到控制台的东西实际上都被 console.log 所包围。

```js
console.log(eval("3 + 5"));
```

即在输入完表达式后，按`Enter`键就会执行。

#### 多行模式

Web 控制台的单行模式非常适合用来测试单个的 JavaScript 表达式，对于复杂的 JavaScript 表达式或者一定规模的代码块就显得力不从心了。这正是多行模式要解决的！

具体看所使用的浏览器是否支持此模式——可以多行输入后，在执行。

如果浏览器没有此模式，可以使用`Shift`+`Enter`的方式来换行，避免在没有输入结束时按`Enter`键就提前运行了。

```js
(function () {
  "use strict";
  function greetMe(yourName) {
    alert("Hello " + yourName);
  }

  greetMe("World");
})();

```

使用浏览器的开发者工具使用JavaScript时，请记住，始终将 `(function(){"use strict";` 添加到你的代码之前，始终将`})();`添加到你的代码之后，这是用于开启**严格模式**（前者）和**立即调用函数表达式**（后者）（IIFE，是一个在定义时就会立即执行的JavaScript函数的）。现在关于它们的作用你只要知道以下两点：

1. 防止 JavaScript 的语义影响初学者
2. 防止控制台中的代码片段之间发生意料之外的交互

### JavaScript和ECMAScript规范

JavaScript 的标准化组织是 [ECMA](https://www.ecma-international.org/)——这个欧洲信息与通信系统标准化协会提供基于 Javascript 的标准化方案（ECMA 原先是欧洲计算机制造商协会的首字母缩写）。这种标准化版本的 JavaScript 被称作 ECMAScript，在所有支持该标准的应用中以相同的方式工作。公司可以使用开放标准语言来开发他们自己的 JavaScript 实现版本。ECMAScript 标准在 ECMA－262 规范中进行文档化。

ECMA-262 标准也通过了 国际标准化组织（ISO）的 ISO-16262。ECMAScript 规范并没有描述文档对象模型（DOM），该模型由万维网联盟（[W3C](https://www.w3.org/)）制定。DOM 定义了 HTML 文件对象被脚本操作的方法。

ECMAScript 规范是实现 ECMAScript 的一组需求;如果你想在 ECMAScript 实现或引擎 (如 Firefox 中的 SpiderMonkey 或 Chrome 中的 V8) 中实现符合标准的语言特性，那么它是非常有用的。

ECMAScript 文档不是用来帮助脚本程序员的;使用 JavaScript 文档获取关于编写脚本的信息。

ECMAScript 规范使用了 JavaScript 程序员可能不熟悉的术语和语法。尽管 ECMAScript 中对语言的描述可能有所不同，但语言本身保持不变。JavaScript 支持 ECMAScript 规范中列出的所有功能。

JavaScript 文档描述了适合 JavaScript 程序员的语言方面。

## 语法和数据类型

JavaScript 借鉴了 Java 的大部分语法，但同时也受到 Awk、Perl 和 Python 的影响。

JavaScript 是**区分大小写**（或者说是大小写敏感）的，并使用 **Unicode** 字符集。

在 JavaScript 中，指令被称为**语句**，并用分号`;`进行分隔。如果一条语句独占一行的话，那么分号是可以省略的。（并不建议这么做）但如果一行中有多条语句，那么这些语句必须以分号分开。

**Javascript 源码从左往右被扫描并转换成一系列由 token、控制字符、行终止符、注释和空白字符组成的输入元素。空白字符指的是空格、制表符和换行符等**。

### 注释

**Javascript 注释**的语法和 C++ 或许多其他语言类似：

```
// 单行注释

/* 这是一个更长的，
   多行注释
*/

/* 然而，你不能，/* 嵌套注释 */ 语法错误 */

```

*注：你可能会在一些 JavaScript 脚本中见到像这样 `#!/usr/bin/env node` 的第三种注释。这种注释我们称为**hashbang 注释**，这种注释被用来指定执行 JaveScript 脚本的引擎的路径。*

### 变量与声明

在应用程序中，使用**变量**来作为值的符号名。变量的名字又叫做**标识符**，其需要遵守一定的规则。

**一个 JavaScript 标识符必须以字母、下划线（_）或者美元符号（$）开头；后续的字符也可以是数字（0-9）。因为 JavaScript 语言是区分大小写的，所以字母可以是从“A”到“Z”的大写字母和从“a”到“z”的小写字母**。

JavaScript 有三种**声明方式**。

+ `var`

  声明一个变量，可初始化一个值。

+ `let`

  声明一个**块作用域的局部变量**，可以初始化一个值。

+ `const`

  声明一个**块作用域的只读常量**。

你可以用以下三种方式**声明变量**：

- 使用关键词 `var` 。例如 `var x = 42`。这个语法可以用来声明局部变量和全局变量。
- 直接赋值。例如 `x = 42`。在函数外使用这种形式赋值，会产生一个全局变量。在严格模式下会产生错误。因此你不应该使用这种方式来声明变量。
- 使用关键词 `let` 。例如 `let y = 13`。这个语法可以用来声明块作用域的局部变量。

你可以使用**解构赋值**将**对象字面量的属性绑定到变量**。就像这样 `let { bar } = foo`。这会创建一个名为 `bar` 的变量，并且将 `foo` **对象中属性名与之相同的属性的值赋给它**。

你也可以**直接给属性赋值**。像这样 `x = 42`。这种声明方式将会创建一个**未声明全局变量**。这样做还会产生 JavaScript 警告。**因为未声明的全局变量常常导致预期之外的行为，所以不建议使用**。

### 变量初值——`undefined`

用 `var` 或 `let` 语句声明的变量，如果没有赋初始值，则其值为 `undefined`。

如果**访问一个未声明的变量**会导致抛出 `ReferenceError`异常：

```js
var a;
console.log("The value of a is " + a); // a 的值是 undefined

console.log("The value of b is " + b); // b 的值是 undefined
var b;	// 在你阅读下面的‘变量声明提升’前你可能会疑惑

console.log("The value of c is " + c); // 未捕获的引用错误：c 未被定义

let x;
console.log("The value of x is " + x); // x 的值是 undefined

console.log("The value of y is " + y); // 未捕获的引用错误：y 未被定义
let y;

```

你可以**使用 `undefined` 来判断一个变量是否已赋值**。在以下的代码中，变量`input`未被赋值，因此`if` 条件语句的求值结果是 `true`。

```js
var input;
if (input === undefined) {
  doThis();
} else {
  doThat();
}

```

`undefined` 值在**布尔类型环境**中会被当作 `false` 。例如，下面的代码将会执行函数 `myFunction`，因为数组 `myArray` 中的元素未被赋值：

```js
var myArray = [];
if (!myArray[0]) myFunction();

```

`undefined` 值在数值类型环境中 `undefined` 值会被转换为 `NaN`。

```java
var a;
a + 2; // 计算为 NaN

```

当你对一个 `null`变量求值时，空值 `null` 在数值类型环境中会被当作 0 来对待，而布尔类型环境中会被当作 `false`。例如：

```js
var n = null;
console.log(n * 32); // 在控制台中会显示 0

```



### 变量的作用域

在函数之外声明的变量，叫做**全局变量**，因为它可被当前文档中的任何其他代码所访问。

在函数内部声明的变量，叫做**局部变量**，因为它只能在当前函数的内部访问。

**ECMAScript 6 之前的 JavaScript 没有语句块作用域**；ECMAScript 6 及之后的JavaScript中语句块中声明的变量将成为语句块所在函数（或全局作用域）的局部变量。

例如，如下的代码将在控制台（ECMAScript 6 之前）输出 5，因为 `x` 的作用域是声明了 `x` 的那个函数（或全局范围），而不是 `if` 语句块。

```js
if (true) {
  var x = 5;
}
console.log(x); // 5

```

如果使用 ECMAScript 6 中的 `let` 声明，上述行为将发生变化。

```js
if (true) {
  let y = 5;
}
console.log(y); // ReferenceError: y 没有被声明

```



### 变量提升

JavaScript 变量的另一个不同寻常的地方是，你**可以先使用变量稍后再声明变量而不会引发异常，这一概念称为变量提升**。

JavaScript 变量感觉上是被“提升”或移到了函数或语句的最前面。但是，**提升后的变量将返回 undefined 值**。因此**在使用或引用某个变量之后进行声明和初始化操作，这个被提升的变量仍将返回 undefined 值**。

```
/**
 * 例子 1
 */
console.log(x === undefined); // true
var x = 3;

/**
 * 例子 2
 */
// will return a value of undefined
var myvar = "my value";

(function () {
  console.log(myvar); // undefined
  var myvar = "local value";
})();

```

上面的例子，也可写作：

```
/**
 * 例子 1
 */
var x;
console.log(x === undefined); // true
x = 3;

/**
 * 例子 2
 */
var myvar = "my value";

(function () {
  var myvar;
  console.log(myvar); // undefined
  myvar = "local value";
})();

```

注意写法，下例不为`undefined`:

```js
var myName = "zhangsan";
(function(){
    console.log(myName); //zhangsan
    myName = "lisi";
})();
```

由于存在变量提升，一个函数中所有的`var`语句应尽可能地放在接近函数顶部的地方。这个习惯将大大提升代码的清晰度。

在 ECMAScript 6 中，`let` 和 `const` 同样**会被提升**变量到代码块的顶部但是不会被赋予初始值。在变量声明之前引用这个变量，将抛出引用错误（ReferenceError）。这个变量将从代码块一开始的时候就处在一个“暂时性死区”，直到这个变量被声明为止。

```js
console.log(x); // ReferenceError
let x = 3;

```

### 函数提升

对于函数来说，只有函数声明会被提升到顶部，而函数表达式不会被提升。

```js
/* 函数声明 */

foo(); // "bar"

function foo() {
  console.log("bar");
}

/* 函数表达式 */

baz(); // 类型错误：baz 不是一个函数

var baz = function () {
  console.log("bar2");
};

```



### 全局变量

实际上，**全局变量是全局对象的属性**。在网页中，（缺省的）全局对象是 `window` ，所以你可以用形如 `window.variable` 的语法来设置和访问全局变量。

因此，你可以通过指定 window 或 frame 的名字，在当前 window 或 frame 访问另一个 window 或 frame 中声明的变量。例如，在文档里声明一个叫 `phoneNumber` 的变量，那么你就可以在子框架里使用 `parent.phoneNumber` 的方式来引用它。

### 常量

你可以用关键字 `const` 创建一个只读的常量。常量标识符的命名规则和变量相同：必须以字母、下划线（_）或美元符号（$）开头并可以包含有字母、数字或下划线。

```js
const PI = 3.14;
```

**常量不可以通过重新赋值改变其值，也不可以在代码运行时重新声明。它必须被初始化为某个值**。

常量的作用域规则与 `let` 块级作用域变量相同。若省略 `const` 关键字，则该标识符将被视为变量。

在同一作用域中，不能使用与变量名或函数名相同的名字来命名常量：

```js
// 这会造成错误
function f() {}
const f = 5;

// 这也会造成错误
function f() {
  const g = 5;
  var g;

  //语句
}

```

+ 然而，对象属性被赋值为常量是不受保护的，所以下面的语句执行时不会产生错误。

  ```js
  const MY_OBJECT = { key: "value" };
  MY_OBJECT.key = "otherValue";
  ```

+ 同样的，数组的被定义为常量也是不受保护的，所以下面的语句执行时也不会产生错误。

  ```js
  const MY_ARRAY = ["HTML", "CSS"];
  MY_ARRAY.push("JAVASCRIPT");
  console.log(MY_ARRAY); //logs ['HTML','CSS','JAVASCRIPT'];
  ```



### 数据类型

最新的 ECMAScript 标准定义了 8 种数据类型：

+ 7种基本数据类型：
  + 布尔值（Boolean），有两个值分别是：`true`和`false`。
  + `null`，一个表明null值的特殊关键字。JavaSCript是大小写敏感的，因此`null`与`Null`、`NULL`或变体完全不同。
  + `undefined`，和 null 一样是一个特殊的关键字，`undefined` 表示变量未赋值时的属性。
  + 数字（Number），整数或浮点数，例如：`42`或者`3.14159`。
  + 任意精度的整数（BigInt），可以安全地存储和操作大整数，甚至可以超过数字的安全整数限制。
  + 字符串（String），字符串是一串表示文本值的字符序列，例如：`Howdy`。
  + 代表（Symbol），在 ECMAScript 6 中新添加的类型，一种实例是唯一且不可改变的数据类型。
+ 对象（Object）。

虽然这些数据类型相对来说比较少，但是通过他们你可以在程序中开发有用的功能。对象和函数是这门语言的另外两个基本元素。你可以把对象当作存放值的一个命名容器，然后将函数当作你的程序能够执行的步骤。

### 数据类转换

JavaScript 是一种动态类型语言 (dynamically typed language)。这意味着你**在声明变量时可以不必指定数据类型，而数据类型会在代码执行时会根据需要自动转换**。例如：

```js
var answer = 44;
answer = "World";
```

因为 JavaScript 是动态类型的，这种赋值方式并不会提示出错。

#### 数字转换为字符串

**在包含的数字和字符串的表达式中使用加法运算符（+），JavaScript 会把数字转换成字符串**。例如，观察以下语句：

```js
x = "The answer is " + 42; // "The answer is 42"
y = 42 + " is the answer"; // "42 is the answer"
```

在涉及其他运算符时，JavaScript 语言不会把数字变为字符串。例如：

```js
"37" - 7; // 30
"37" + 7; // "377"
```



#### 字符串转换为数字

有一些方法可以将内存中表示一个数字的字符串转换为对应的数字。

+ `parseInt()`
+ `parseFloat()`

`parseInt` 方法只能返回整数，所以使用它会丢失小数部分。另外，调用 parseInt 时最好总是带上进制（radix）参数，这个参数用于指定使用哪一种进制。

将字符串转换为数字的另一种方式就是使用一元加法运算符。

```js
"1.1" + "1.1" = "1.11.1";
(+"1.1") + (+"1.1") = 2.2;// 注意：加入括号为清楚起见，不是必需的。
```



### 字面量

在 JavaScript 中，你可以使用各种字面量。这些字面量是脚本中按字面意思给出的固定的值，而不是变量。

#### 数组字面量

数组字面值是一个封闭在方括号`[]`中的包含有零个或多个表达式的列表，其中每个表达式代表数组的一个元素。当你使用数组字面值创建一个数组时，该数组将会以指定的值作为其元素进行初始化，而其长度被设定为元素的个数。

```js
var coffees = ["French Roast", "Colombian", "Kona"];
var a = [3];

console.log(a.length); // 1
console.log(a[0]); // 3
```

若在顶层（全局）脚本里用字面值创建数组，JavaScript 语言将会在每次对包含该数组字面值的表达式求值时解释该数组。另一方面，在函数中使用的数组，将在每次调用函数时都会被创建一次。

不必列举数组字面值中的所有元素。若你在同一行中连写两个逗号`,`，数组中就会产生一个没有被指定的元素，其初始值是 `undefined`。以下示例创建了一个名为 `fish` 的数组：

```js
var fish = ["Lion", , "Angel"];
```

在这个数组中，有两个已被赋值的元素，和一个空元素（fish[0] 是 "Lion"，fish[1] 是 undefined，而 fish[2] 是 "Angel"）。

如果你在元素列表的尾部添加了一个逗号，它将会被忽略。在下面的例子中，数组的长度是 3，并不存在 myList[3] 这个元素。元素列表中其他所有的逗号都表示一个新元素（的开始）。

```js
var fish = ["Lion", ,"Angel",];
```

*注：尾部的逗号在早期版本的浏览器中会产生错误，因而编程时的最佳实践方式就是移除它们。*

在下面的例子中，数组长度为4，元素`myList[0]`和`myList[2]`缺失。

```js
var myList = [, "home", , "school"];
```

再看一个例子。在这里，该数组的长度是 4，元素 `myList[1]` 和 `myList[3]` 被漏掉了。（但是）只有最后的那个逗号被忽略。

```js
var myList = ["home", , "school", ,];
```

理解多余的逗号（在脚本运行时会被如何处理）的含义，对于从语言层面理解 JavaScript 是十分重要的。但是，在你自己写代码时：**显式地将缺失的元素声明为 `undefined`，将大大提高你的代码的清晰度和可维护性**。

#### 布尔字面量

布尔类型有两种字面量：`true`和`false`。

**不要混淆作为布尔对象的真和假与布尔类型的原始值 true 和 false。布尔对象是原始布尔数据类型的一个包装器。**

#### 数字字面量

JavaScript数字字面量包括**多种基数的整数字面量**和**以10为基数的浮点数字面量**。

值得一提的是，语言标准要求数字字面量必须是无符号的。但是像`-123.4`这样的代码片段还是没有问题的，会被解释为一元操作符`-`应用于数字字面量`123.4`。

##### 整数字面量

整数可以用十进制（基数为 10）、十六进制（基数为 16）、八进制（基数为 8）以及二进制（基数为 2）表示。

+ 十进制整数字面量由一串数字序列组成，且没有前缀`0`（零）。
+ 八进制的整数以`0`（零，或`0O`{零大写字母O}、`0o`{零小写字母o）开头，只能包括数字`0-7`。
+ 十六进制整数以`0x`（零x，或`0X`）开头，可以包含数字`0-9`和字母`a-f`或`A-F`。
+ 二进制整数以`0b`（或`0B`）开头，只能包含数字`0`和`1`。

严格模式下，八进制整数字面量必须以` 0o` 或` 0O `开头，而不能以` 0` 开头。

整数字面量举例：

```
0, 117 and -345 (十进制，基数为 10)
015, 0001 and -0o77 (八进制，基数为 8)
0x1123, 0x00111 and -0xF1A7 (十六进制，基数为 16 或"hex")
0b11, 0b0011 and -0b11 (二进制，基数为 2)
```

##### 浮点数字面量

浮点数字面值可以有以下的组成部分：

+ 一个十进制整数，可以带正负号（即前缀`+`或`-`）
+ 小数点（`.`）
+ 小数部分（由一串十进制数表示）
+ 指数部分。以`e`或`E`开头，后面跟着一个整数，可以有正负号（即前缀`+`或`-`）

其语法为：

```js
[(+|-)][digits][.digits][(E|e)[(+|-)]digits]
```

例如：

```js
3.1415926
.123456789
3.1E+12
.1e-23
```



#### 对象字面量

对象字面值是封闭在花括号对`{}`中的一个对象的零个或多个`属性名-值`对的（元素）列表。

**警告：你不能在一条语句的开头就使用对象字面值，这将导致错误或产生超出预料的行为，因为此时左花括号（{）会被认为是一个语句块的起始符号。**

以下是一个对象字面值的例子。对象`car`的第一个元素（译注：即一个属性/值对）定义了属性 `myCar`；第二个元素，属性 `getCar`，引用了一个函数调用（即 CarTypes("Honda")）；第三个元素，属性 `special`，使用了一个已有的变量（即 Sales）。

```js
var Sales = "Toyota";

function CarTypes(name) {
  return name === "Honda" ? name : "Sorry, we don't sell " + name + ".";
}

var car = { myCar: "Saturn", getCar: CarTypes("Honda"), special: Sales };

console.log(car.myCar); // Saturn
console.log(car.getCar); // Honda
console.log(car.special); // Toyota
```

更进一步的，你可以使用数字或字符串字面值作为属性的名字，或者在另一个字面值内嵌套上一个字面值。如下的示例中使用了这些可选项。

```js
var car = { manyCars: { a: "Saab", b: "Jeep" }, 7: "Mazda" };

console.log(car.manyCars.b); // Jeep
console.log(car[7]); // Mazda
```

对象**属性名字可以是任意字符串，包括空串**。**如果对象属性名字不是合法的javascript 标识符，它必须用引号包裹**。

**属性的名字不合法，那么便不能用点（`.`）访问属性值，而是通过方括号表示法（`[]`）来访问**。

```js
const unusualPropertyNames = {
  '': '空字符串',
  '!': '砰！'
}
console.log(unusualPropertyNames.'');   // SyntaxError: Unexpected string
console.log(unusualPropertyNames.!);    // SyntaxError: Unexpected token !

console.log(unusualPropertyNames[""]); // 空字符串
console.log(unusualPropertyNames["!"]); // 砰！
```



##### 增强的对象字面量

在 ES2015，对象字面值扩展支持在创建时设置原型，简写了 foo: foo 形式的属性赋值，方法定义，支持父方法调用，以及使用表达式动态计算属性名。总之，这些也使对象字面值和类声明更加紧密地联系起来，让基于对象的设计从这些便利中更加受益。

```js
var obj = {
  // __proto__
  __proto__: theProtoObj,
  // Shorthand for ‘handler: handler’
  handler,
  // Methods
  toString() {
    // Super calls
    return "d " + super.toString();
  },
  // Computed (dynamic) property names
  ["prop_" + (() => 42)()]: 42,
};
```

注意：

```js
var foo = { a: "alpha", 2: "two" };
console.log(foo.a); // alpha
console.log(foo[2]); // two
//console.log(foo.2);  // SyntaxError: missing ) after argument list
//console.log(foo[a]); // ReferenceError: a is not defined
console.log(foo["a"]); // alpha
console.log(foo["2"]); // two
```



#### RegExp字面值

一个正则表达式(regular expression)是字符被斜线（正斜杠`/`）围成的表达式。下面是一个正则表达式文字的一个例子。

```js
var re = /ab+c/;
```



#### 字符串字面量

**字符串字面量是由双引号（`"`）对或单引号（`'`）括起来的零个或多个字符**。字符串被限定在同种引号之间；也即，必须是成对单引号或成对双引号。下面的例子都是字符串字面值：

```js
'foo'
"bar"
'1234'
'one line \n another line'
"Joyo's cat"
```

你可以在字符串字面值上使用字符串对象的所有方法——JavaScript 会自动将字符串字面值转换为一个临时字符串对象，调用该方法，然后废弃掉那个临时的字符串对象。你也能用对字符串字面值使用类似 String.length 的属性：

```js
console.log("John's cat".length);
// 将打印字符串中的字符个数（包括空格）
// 结果为：10
```

在 ES2015 中，还提供了一种[模板字面量](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Template_literals)，模板字符串提供了一些语法糖来帮你构造字符串。这与 Perl、Python 还有其他语言中的字符串插值的特性非常相似。除此之外，你可以在通过模板字符串前添加一个 tag 来自定义模板字符串的解析过程，这可以用来防止注入攻击，或者用来建立基于字符串的高级数据抽象。

```js
// Basic literal string creation
`In JavaScript '\n' is a line-feed.` // Multiline strings
`In JavaScript this is
 not legal.`;

// String interpolation
var name = "Bob",
  time = "today";
`Hello ${name}, how are you ${time}?`;

// Construct an HTTP request prefix is used to interpret the replacements and construction
POST`http://foo.org/bar?a=${a}&b=${b}
     Content-Type: application/json
     X-Credentials: ${credentials}
     { "foo": ${foo},
       "bar": ${bar}}`(myOnReadyStateChangeHandler);
```

除非有特别需要使用字符串对象，否则，你应当始终使用字符串字面值。

##### 特殊字符和转义字符

| 字符               | 意思                                                         |
| ------------------ | ------------------------------------------------------------ |
| \0                 | Null字符                                                     |
| \b                 | 退格符                                                       |
| \f                 | 换页符                                                       |
| \n                 | 换行符                                                       |
| \r                 | 回车符                                                       |
| \t                 | Tab（制表符）                                                |
| \v                 | 垂直制表符                                                   |
| \\'                | 单引号                                                       |
| \\"                | 双引号                                                       |
| \\\                | 反斜杠字符（\\)                                              |
| \XXX               | 由从 0 到 377 最多三位八进制数*XXX*表示的 Latin-1 字符。例如，\251 是版权符号的八进制序列。 |
| \xXX               | 由从 00 和 FF 的两位十六进制数字 XX 表示的 Latin-1 字符。例如，\ xA9 是版权符号的十六进制序列。 |
| \uXXXX             | 由四位十六进制数字 XXXX 表示的 Unicode 字符。例如，\ u00A9 是版权符号的 Unicode 序列。 |
| \u*<br />{XXXXX}\* | Unicode 代码点 (code point) 转义字符。例如，\u{2F804} 相当于 Unicode 转义字符 \uD87E\uDC04 的简写。 |

Javascript 没有“heredoc”语法，但可以用行末的换行符转义和转义的换行来近似实现.

```js
var poem =
  "Roses are red,\n\
Violets are blue.\n\
Sugar is sweet,\n\
and so is foo.";
```



## 流程控制与错误处理

### 语句块

最基本的语句(statement)是用于组合语句的语句块。该块由一对大括号界定：

```
{
   statement_1;
   statement_2;
   statement_3;
   .
   .
   .
   statement_n;
}
```

**注意**：**在 ECMAScript 6 标准之前，Javascript 没有块作用域**。在一个块中引入的变量的作用域是包含函数或脚本，并且设置它们的效果会延续到块之外。换句话说，块语句不定义范围。JavaScript 中的“独立”块会产生与 C 或 Java 中完全不同的结果。

```js
var x = 1;
{
  var x = 2;
}
alert(x); // 输出的结果为 2
```

这段代码的输出是**2**，这是因为块级作用域中的 var x 变量声明与之前的声明在同一个作用域内。在 C 语言或是 Java 语言中，同样的代码输出的结果是 1。

从 ECMAScript 2015 开始，使用 `let` 和`const`变量是块作用域的。

### 条件判断语句

条件判断语句指的是根据指定的条件所返回的结果（真或假或其他预定义的），来执行特定的语句。JavaScript 支持两种条件判断语句：`if...else`和`switch`。

#### `if...else`语句

当一个逻辑条件为真，用 if 语句执行一个语句。当这个条件为假，使用可选择的 else 从句来执行这个语句。`if`语句如下：

```js
if (condition) {
  statement_1;
} else {
  statement_2;
} //推荐使用严格的语句块模式，语句 else 可选
```

条件可以是任何返回结果被计算为 true 或 false 的表达式。如果条件表达式返回的是 true，statement_1 语句会被执行；否则，statement_2 被执行。statement_1 和 statement_2 可以是任何语句，甚至你可以将另一个 if 语句嵌套其中。

你也可以组合语句通过使用 `else if` 来测试连续多种条件判断，就像下面一样：

```js
if (condition_1) {
  statement_1;
} else if (condition_2) {
  statement_2;
} else if (condition_n_1) {
  statement_n;
} else {
  statement_last;
}
```

下面这些值将被计算出`false`：

+ `false`
+ `undefined`
+ `null`
+ `0`
+ `NaN`
+ 空字符串（`""`）

当传递给条件语句所有其他的值，包括所有对象会被计算为真。

请不要混淆原始的布尔值`true`和`false` 与 [`Boolean`](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Boolean)对象的真和假。例如：

```js
var b = new Boolean(false);
if (b) //结果视为真
if (b == true) // 结果视为假
```



#### `switch`语句

`switch` 语句允许一个程序求一个表达式的值并且尝试去匹配表达式的值到一个 `case` 标签。如果匹配成功，这个程序执行相关的语句。`switch` 语句如下所示：

```js
switch (expression) {
   case label_1:
      statements_1
      [break;]
   case label_2:
      statements_2
      [break;]
   ...
   default:
      statements_def
      [break;]
}
```

程序首先查找一个与 `expression` 匹配的 `case` 语句，然后将控制权转移到该子句，执行相关的语句。如果没有匹配值，程序会去找 `default` 语句，如果找到了，控制权转移到该子句，执行相关的语句。如果没有找到 `default`，程序会继续执行 `switch` 语句后面的语句。`default` 语句通常出现在 switch 语句里的最后面，当然这不是必须的。

`可选的 break` 语句与每个 `case` 语句相关联，保证在匹配的语句被执行后程序可以跳出 `switch` 并且继续执行 `switch` 后面的语句。如果 break 被忽略，则程序将继续执行 switch 语句中的下一条语句。

### 异常处理语句

可以用`throw`语句抛出一个异常并且用`try...catch`语句捕获处理它。

+ `throw`语句
+ `try...catch`语句

#### 异常类型

JavaScript可以抛出任意对象。然而，不是所有对象能产生相同的结果。尽管抛出数值或者字母串作为异常信息十分常见，但是通常用下列其中一种异常类型来创建目标更为高效。

+ ECMAScript exceptions
+ DOMException 和 DOMError

#### `throw`语句

使用`throw`语句抛出一个异常。当你抛出异常，你规定一个含有值的表达式要被抛出。

```js
throw expression;
```

你可以抛出任意表达式而不是特定一种类型的表达式。下面的代码抛出了几个不同类型的表达式：

```js
throw "Error2"; // String type
throw 42; // Number type
throw true; // Boolean type
throw {
  toString: function () {
    return "I'm an object!";
  },
};
```

*注：可以在抛出异常时声明一个对象，这样就可以在`catch`块中查询到对象的属性。*

````js
// Create an object type UserException
function UserException(message) {
  this.message = message;
  this.name = "UserException";
}

// Make the exception convert to a pretty string when used as
// a string (e.g. by the error console)
UserException.prototype.toString = function () {
  return this.name + ': "' + this.message + '"';
};

// Create an instance of the object type and throw it
throw new UserException("Value too high");
````



#### `try...catch`语句

`try...catch` 语句标记一块待尝试的语句，并规定一个以上的响应应该有一个异常被抛出。如果我们抛出一个异常，`try...catch`语句就捕获它。

`try...catch` 语句有一个包含一条或者多条语句的 try 代码块，0 个或 1 个的`catch`代码块，catch 代码块中的语句会在 try 代码块中抛出异常时执行。换句话说，如果你在 try 代码块中的代码如果没有执行成功，那么你希望将执行流程转入 catch 代码块。如果 try 代码块中的语句（或者`try` 代码块中调用的方法）一旦抛出了异常，那么执行流程会立即进入`catch` 代码块。如果 try 代码块没有抛出异常，catch 代码块就会被跳过。`finally` 代码块总会紧跟在 try 和 catch 代码块之后执行，但会在 try 和 catch 代码块之后的其他代码之前执行。

下面的例子使用了`try...catch`语句。示例调用了一个函数用于从一个数组中根据传递值来获取一个月份名称。如果该值与月份数值不相符，会抛出一个带有`"InvalidMonthNo"`值的异常，然后在捕捉块语句中设`monthName`变量为`unknown`。

```js
function getMonthName(mo) {
  mo = mo - 1; // Adjust month number for array index (1 = Jan, 12 = Dec)
  var months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
  ];
  if (months[mo]) {
    return months[mo];
  } else {
    throw "InvalidMonthNo"; //throw keyword is used here
  }
}

try {
  // statements to try
  monthName = getMonthName(myMonth); // function could throw exception
} catch (e) {
  monthName = "unknown";
  logMyErrors(e); // pass exception object to error handler -> your own function
}
```



#### `catch`块

可以使用`catch`块来处理所有可能在`try`块中产生的异常。

```js
catch (catchID) {
  statements
}
```

捕捉块指定了一个标识符（上述语句中的`catchID`）来存放抛出语句指定的值；你可以用这个标识符来获取抛出的异常信息。在插入`throw`块时 JavaScript 创建这个标识符；标识符只存在于`catch`块的存续期间里；当`catch`块执行完成时，标识符不再可用。

#### `finally`块

`finally`块包含了在 try 和 catch 块完成后、下面接着 try...catch 的语句之前执行的语句。`finally`块无论是否抛出异常都会执行。如果抛出了一个异常，就算没有异常处理，`finally`块里的语句也会执行。

你可以用`finally`块来令你的脚本在异常发生时优雅地退出；举个例子，你可能需要在绑定的脚本中释放资源。接下来的例子用文件处理语句打开了一个文件（服务端的 JavaScript 允许你进入文件）。如果在文件打开时一个异常抛出，`finally`块会在脚本错误之前关闭文件。

```js
openMyFile();
try {
  writeMyFile(theData); //This may throw a error
} catch (e) {
  handleError(e); // If we got a error we handle it
} finally {
  closeMyFile(); // always close the resource
}
```

如果`finally`块返回一个值，该值会是整个`try-catch-finally`流程的返回值，不管在`try`和`catch`块中语句返回了什么：

```js
function f() {
  try {
    console.log(0);
    throw "bogus";
  } catch (e) {
    console.log(1);
    return true; // this return statement is suspended
    // until finally block has completed
    console.log(2); // not reachable
  } finally {
    console.log(3);
    return false; // overwrites the previous "return"
    console.log(4); // not reachable
  }
  // "return false" is executed now
  console.log(5); // not reachable
}
f(); // console 0, 1, 3; returns false
```

用`finally`块覆盖返回值也适用于在`catch`块内抛出或重新抛出的异常：

```js
function f() {
  try {
    throw "bogus";
  } catch (e) {
    console.log('caught inner "bogus"');
    throw e; // this throw statement is suspended until
    // finally block has completed
  } finally {
    return false; // overwrites the previous "throw"
  }
  // "return false" is executed now
}

try {
  f();
} catch (e) {
  // this is never reached because the throw inside
  // the catch is overwritten
  // by the return in finally
  console.log('caught outer "bogus"');
}

// OUTPUT
// caught inner "bogus"
```



#### 嵌套`try...catch`语句

你可以嵌套一个或多个`try ... catch`语句。如果一个内部`try ... catch`语句没有`catch`块，它需要有一个`finally`块，并且封闭的`try ... catch`语句的`catch`块被检查匹配。

#### 使用`Error`对象

根据错误类型，你也许可以用`name`和`message`获取更精炼的信息。`name`提供了常规的错误类（如 `DOMException'`或 `Error`），而`message`通常提供了一条从错误对象转换成字符串的简明信息。

在抛出你个人所为的异常时，为了充分利用那些属性（比如你的`catch`块不能分辨是你个人所为的异常还是系统的异常时），你可以使用 `Error`构造函数。比如：

```js
function doSomethingErrorProne () {
  if (ourCodeMakesAMistake()) {
    throw (new Error('The message'));
  } else {
    doSomethingToGetAJavascriptError();
  }
}
....
try {
  doSomethingErrorProne();
}
catch (e) {
  console.log(e.name); // logs 'Error'
  console.log(e.message); // logs 'The message' or a JavaScript error message)
}
```



## 循环与迭代

循环有很多种类，但本质上它们都做的是同一件事：它们把一个动作重复了很多次（实际上重复的次数有可能为 0）。各种循环机制提供了不同的方法去确定循环的开始和结束。不同情况下，某一种类型循环会比其他的循环用起来更简单。

JavaScript中提供了这些循环语句：

+ `for`语句
+ `do...while`语句
+ `while`语句
+ `label`语句
+ `break`语句
+ `continue`语句
+ `for...in`语句
+ `for...of`语句

### `for`语句

一个 `for`循环会一直重复执行，直到指定的循环条件为 false。JavaScript 的 for 循环，和 Java、C 的 for 循环，是很相似的。一个 for 语句是这个样子的：

```
for ([initialExpression]; [condition]; [incrementExpression])
  statement
```

当一个 `for` 循环执行的时候，会发生以下过程：

1. 如果有初始化表达式 `initialExpression`，它将被执行。这个表达式通常会初始化一个或多个循环计数器，但语法上是允许一个任意复杂度的表达式的。这个表达式也可以声明变量。
2. 计算 `condition` 表达式的值。如果 `condition` 的值是 true，循环中的语句会被执行。如果 `condition` 的值是 false，`for` 循环终止。如果 `condition` 表达式整个都被省略掉了，condition 的值会被认为是 true。
3. 循环中的 `statement` 被执行。如果需要执行多条语句，可以使用块（`{ ... }`）来包裹这些语句。
4. 如果有更新表达式 `incrementExpression`，执行更新表达式。
5. 回到步骤 2。

### `do...while`语句

`do...while`语句一直重复直到指定的条件求值得到假值（`false`）。一个`do...while`语句看起来像这样：

```js
do
  statement
while (condition);
```

`statement` 在检查条件之前会执行一次。要执行多条语句（语句块），要使用块语句（`{ ... }`）包括起来。如果 `condition` 为真（true），`statement` 将再次执行。在每个执行的结尾会进行条件的检查。当 `condition` 为假（false），执行会停止并且把控制权交回给 `do...while` 后面的语句。

### `while`语句

一个`while`语句只要指定的条件求值为真（`true`）就会一直执行它的语句块。一个`while`语句看起来像这样：

```js
while (condition)
  statement
```

如果这个条件变为假，循环里的 `statement` 将会停止执行并把控制权交回给 `while` 语句后面的代码。

条件检测会在每次 `statement` 执行之前发生。如果条件返回为真， `statement` 会被执行并紧接着再次测试条件。如果条件返回为假，执行将停止并把控制权交回给 while 后面的语句。

要执行多条语句（语句块），要使用语句块 (`{ ... }`) 包括起来。

### `label`语句

一个`label`提供了一个让你在程序中其他位置引用它的标识符。例如，你可以用`label`标识一个循环，然后使用`break`或者`continue`来指出程序是否该停止循环还是继续循环。

`label`语句的语法看起来像这样：

```js
label :
   statement
```

`label`的值可以是任何的非保留字的JavaScript标识符，`statement`可以是任意你想要标识的语句（块）。

在这个例子里，标记 `outPoint` 标识了一个 `for` 循环。使用 continue 语句，则可达到与未添加 label 相同的效果，但在这种有多层循环的情况下，循环的跳出进入流程更为明晰一些：

```js
var num = 0;
outPoint: for (var i = 0; i < 10; i++) {
  for (var j = 0; j < 10; j++) {
    if (i == 5 && j == 5) {
      continue outPoint;
    }
    num++;
  }
}
alert(num); // 95
```

从 alert(num) 的值可以看出，continue outPoint; 语句的作用是跳出当前循环，并跳转到 outPoint（标签）下的 for 循环继续执行。

### `break`语句

使用`break`语句来终止循环、`switch`语句，或者是链接到`label`语句。

+ 当你使用不带`label`的`break`时，它会立即终止当前所在的`while`、`do...while`、`for`，或者`switch`并把控制权交回这些结构后面的语句。
+ 当你使用带`label`的`break`时，它会终止指定的带标记（`label`）的语句。

`break` 语句的语法看起来像这样：

```js
break [label];
```

在语法中，被 `[]` 包裹的内容是可省略的，也就是 `label` 可以省略。若省略，则终止当前所在的循环或 `switch`；若不省略，则终止指定的 label 语句。

### `continue`语句

`continue`语句可以用来继续执行（跳过代码块的剩余部分并进入下一循环）一个`while`、`do...while`、`for`，或者`label`语句。

+ 当你使用不带 label 的 `continue` 时，它终止当前 `while`，`do-while`，或者 for 语句到结尾的这次的循环并且继续执行下一次循环。
+ 当你使用带 label 的 `continue` 时，它会应用被 label 标识的循环语句。

`continue`语句的语法看起来像这样：

```js
continue [label];
```

### `for...in`语句

`for...in`语句循环一个指定的变量来循环一个对象所有可枚举的属性。JavaScript会为每一个不同的属性执行指定的语句。

```js
for (variable in object) {
  statements
}
```

下面的函数通过它的参数得到一个对象和这个对象的名字。然后循环这个对象的所有属性并且返回一个列出属性名和该属性值的字符串。

```js
function dump_props(obj, obj_name) {
  var result = "";
  for (var i in obj) {
    result += obj_name + "." + i + " = " + obj[i] + "<br>";
  }
  result += "<hr>";
  return result;
}
```

#### 数组迭代

虽然使用 **for...in** 来迭代数组 `Array` 元素听起来很诱人，但是它返回的东西除了数字索引外，还有可能是你自定义的属性名字。因此还是用**带有数字索引的传统的 `for`循环来迭代一个数组比较好**，因为，如果你想改变数组对象，比如添加属性或者方法，**for...in** 语句迭代的是自定义的属性，而不是数组的元素。（下面的 `for...of` 语句，和 `forEach()`方法，也是理想的选择。）

### `for...of`语句

`for...of`语句可在可迭代对象（包括`Array`、`Map`、`Set`、`arguments`等等）上创建一个循环，对值的每一个独特属性调用一次迭代。

```js
for (variable of object) {
  statement
}
```

下面的这个例子展示了 `for...of` 和 `for...in`两种循环语句之间的区别。 `for...in` 循环遍历的结果是数组元素的下标，而 `for...of` 遍历的结果是元素的值：

```js
let arr = [3, 5, 7];
arr.foo = "hello";

for (let i in arr) {
  console.log(i); // 输出 "0", "1", "2", "foo"
}

for (let i of arr) {
  console.log(i); // 输出 "3", "5", "7"
}

// 注意 for...of 的输出没有出现 "hello"
```



## 函数

