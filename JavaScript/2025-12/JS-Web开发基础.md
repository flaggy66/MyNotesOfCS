# JavaScript—Web开发基础

## 事件 Event

事件是发生在你正在编程的系统中的事情——当事件发生时，系统产生（或“触发”）某种信号，并提供一种机制，当事件发生时，可以自动采取某种行动（即运行一些代码）。事件是在浏览器窗口内触发的，并倾向于附加到驻留在其中的特定项目。这可能是一个单一的元素，一组元素，当前标签中加载的 HTML 文档，或整个浏览器窗口。

为了对一个事件做出反应，你要给它附加一个**事件处理器**，这是一个代码块（通常是创建的一个 JavaScript 函数），在事件发生时运行。当这样一个代码块被定义为响应一个事件而运行时，则在**注册一个事件处理器**。注意，事件处理器有时候被叫做**事件监听器**。

**web 事件不是 JavaScript 语言的核心——它们被定义成内置于浏览器的API。**



### 添加/删除事件处理器

 使用`addEventListener()`添加事件处理器，这是推荐的**添加事件处理器**的机制。如：

```js
const btn = document.querySelector("button");

btn.addEventListener("click", () => {
  alert("你点击了按钮！");
});
```

除了`click`——点击（单击）事件，还有如：`focus`——聚焦，`blur`——失焦，这些事件通常用于在聚焦时显示填入表单字段的信息，或者在表单字段填入不正确的值时显示错误信息。`dblclick`——双击。`mouseover`——鼠标悬停，`mouseout`——鼠标移出。

一些事件，如 `click`（点击事件），几乎对任何元素都可用。其他事件则更具体，只在某些情况下有用：例如，`play`事件只对某些元素有效，如 `<video>`元素。

如果你使用 `addEventListener()` 添加了一个事件处理器，你可以使用 `removeEventListener()`方法再次**删除事件处理器**。

```js
const btn = document.querySelector("button");

function myHint(){
	alert("你点击了按钮！");
}

// 添加事件处理器
btn.addEventListener("click", myHint);

// 删除事件处理器
btn.removeEventListener("click", myHint);
```

事件处理器也可以通过传递 `AbortSignal`到 `addEventListener()`，然后在拥有 `AbortSignal` 的控制器上调用`abort()`，从而删除事件处理器。

```js
const btn = document.querySelector("button");

const controller = new AbortController();

btn.addEventListener("click",
  () => alert("你点击了按钮！"),
  { signal: controller.signal } // 向该处理器传递 AbortSignal
);

controller.abort(); // 移除任何与该控制器相关的事件处理器
```

对于简单的小程序，清理旧的、未使用的事件处理器是没有必要的，但对于更大的、更复杂的程序，它可以提高效率。另外，删除事件处理器的能力允许你让同一个按钮在不同的情况下执行不同的动作：你所要做的就是添加或删除处理程序。

通过对 `addEventListener()`的多次调用，每次提供不同的处理器，你可以**为一个事件设置多个处理器**：

```js
myElement.addEventListener("click", functionA);
myElement.addEventListener("click", functionB);
```

当点击标签元素时，所有处理器函数都会运行。



### 其他事件监听机制

还有两种注册事件处理器的方法，你可能会看到：**事件处理器属性**和**内联事件处理器**。

可以触发事件的对象（如按钮）通常也有属性，其名称是 `on`，后面是事件的名称。例如，元素有一个属性 **`onclick`**。这被称为**事件处理器属性**。为了监听事件，你可以将处理函数分配给该属性。

```js
const btn = document.querySelector("button");

btn.onclick = () => alert("你点击了按钮！");

// 或使用函数名分配
function myHint(){
	alert("你点击了按钮！");
}

btn.onclick = myHint;
```

**对于事件处理器属性，你不能为一个事件添加一个以上的处理程序。**

对于事件处理器属性来说，这是不可能的，因为任何后续尝试都会覆写较早设置的属性：

```js
element.onclick = function1;
element.onclick = function2;
```



**内联事件处理器不建议使用**，它一般的形式是在HTML标签中设置了元素的事件处理器属性，再在JavaScript中编写对应的事件处理器。如：

HTML文本：

```html
<button onclick="myHint()">按下我</button>
```

JavaScript代码：

```js
function myHint() {
  alert("你点击了按钮！");
}
```

在 web 上发现的最早的注册事件处理器的方法涉及到**事件处理器 HTML 属性**（或**内联事件处理器**），如示例所示。上面的示例调用了同一页面上 `<script>` 元素内定义的一个函数，但你也可以直接在属性内插入 JavaScript，比如说：

```html
<button onclick="alert('你点击了按钮！');">
  按下我
</button>
```

不建议使用这些属性——它们被认为是不好的做法。原因：它会把 HTML 和 JavaScript 混在一起，变得难以阅读。作为一项安全措施，许多常见的服务器配置将禁止内联 JavaScript。



### 事件处理对象

有时候在事件处理函数内部，可能会看到一个固定指定名称的参数，例如 `event`、`evt` 或 `e`。这被称为**事件对象**，它被自动传递给事件处理函数，以提供额外的功能和信息。

```js
const btn = document.querySelector("button");

function myHint(event) {
  alert("你点击了按钮！");
  event.target.style.backgroundColor = red;
  console.log(event);
}

btn.addEventListener("click", myHint);
```

在上述代码中，可以看到在函数中包括一个事件对象 `event`，并在函数中设置背景颜色样式在 `event.target` 上——它指的是按钮本身。事件对象 `event` 的 `target` 属性始终是事件刚刚发生的元素的引用。

可以使用任何喜欢的名称作为事件对象——只需要选择一个名称，然后可以在事件处理函数中引用它。开发人员最常使用 `e`/`evt`/`event`，因为它们很简单易记。

大多数事件对象都有一套标准的属性和方法，请参阅 [Event](https://developer.mozilla.org/zh-CN/docs/Web/API/Event) 对象参考，以获得完整的列表。



需要说明：**网页的 JavaScript 的事件模型与其他环境中使用的 JavaScript 的事件模型也是不同的。例如，`Node.js`是一个非常流行的 JavaScript 运行时，使开发人员能够使用 JavaScript 来构建网络和服务器端应用程序。`Node.js` 事件模型依靠监听器来监听事件，依靠发射器来定期发射事件。听起来没有什么不同，但代码却很不同，利用 `on()` 等函数来注册一个事件监听器，而 `once()` 则是注册一个一次性事件监听器，在运行一次后取消注册。**



### 事件冒泡 & 事件捕获 & 事件委托

有如下的HTML文档片段：

```html
<body>
  <div id="container">
    <button>点我！</button>
  </div>
  <pre id="output"></pre>
</body>
```

将按钮的事件处理器——“显示触发事件绑定对象”添加到`<div>`元素上：

```js
const output = document.querySelector("#output");
function handleClick(e) {
  output.textContent += `你在 ${e.currentTarget.tagName} 元素上进行了点击\n`;
}

const container = document.querySelector("#container");
container.addEventListener("click", handleClick);

```

点击按钮`<button>`后，`<pre>`标签的内容出现`你在 DIV 元素上进行了点击`。虽然`<button>`没有添加事件处理器，但对应的`click`事件在父元素`<div>`中注册了，所以当点击按钮时，按钮的点击事件由父元素`<div>`绑定的事件监听器处理。

现在从内到外，分别给`<button>`、`<div>`、`<body>`添加事件处理器——当点击按钮时，`<pre>`标签内容追加`你在xx元素上进行了点击`：

```js
const output = document.querySelector("#output");
function handleClick(e) {
  output.textContent += `你在 ${e.currentTarget.tagName} 元素上进行了点击\n`;
}

const container = document.querySelector("#container");
const button = document.querySelector("button");

document.body.addEventListener("click", handleClick);
container.addEventListener("click", handleClick);
button.addEventListener("click", handleClick);
```

点击按钮，发现`<pre>`标签的内容如下：

```
你在 BUTTON 元素上进行了点击
你在 DIV 元素上进行了点击
你在 BODY 元素上进行了点击
```

显然地，在触发按钮`<button>`的点击事件后，先处理的是`<button>`元素上的事件处理器，接着是直接父元素`<div>`上的事件处理器，最后是间接父元素`<body>`上的事件处理器。这就是**事件冒泡**，事件从被点击的最里面的元素**冒泡**而出。

**事件冒泡**：事件从目标元素开始，逐层向上传播到最外层的过程。从内而外，是浏览器默认开启的。

有时并不想事件处理一直向外传播，希望它能够传播到某个事件处理后就结束，可以**使用`Event`对象的`stopPropagation()`函数阻止事件冒泡**。

```js
const output = document.querySelector("#output");
function handleClick(e) {
  output.textContent += `你在 ${e.currentTarget.tagName} 元素上进行了点击\n`;
}

const container = document.querySelector("#container");
const button = document.querySelector("button");

document.body.addEventListener("click", handleClick);
container.addEventListener("click", (e) => {
    e.stopPropagation(); // 阻止事件冒泡
    output.textContent += `你在 ${e.currentTarget.tagName} 元素上进行了点击\n`;
});
button.addEventListener("click", handleClick);
```

上述代码，当点击按钮后，`<pre>`标签的内容仅显示在`BUTTON`和`DIV`上点击了，事件并没有向`<body>`元素传播。

事件传播的另一种形式是**事件捕获**：事件从最外层（window / document）向目标元素“传递”的过程。从外到内，浏览器默认不开启，需要显式开启。

事件捕获默认是禁用的，需要**在 `addEventListener()` 的 `capture` 选项中启用事件捕获**。

```js
const output = document.querySelector("#output");
function handleClick(e) {
  output.textContent += `你在 ${e.currentTarget.tagName} 元素上进行了点击\n`;
}

const container = document.querySelector("#container");
const button = document.querySelector("button");

document.body.addEventListener("click", handleClick, { capture: true });
container.addEventListener("click", handleClick, { capture: true });
/* 可以直接省略capture
container.addEventListener("click", handleClick, true);
*/
button.addEventListener("click", handleClick);
```

这次点击按钮，`<pre>`标签的内容显示如下：

```
你在 BODY 元素上进行了点击
你在 DIV 元素上进行了点击
你在 BUTTON 元素上进行了点击
```

**可见事件捕获和事件冒泡的处理顺序是颠倒的**。

**一次 DOM 事件的传播顺序是：事件捕获 → 目标阶段 → 事件冒泡**

```
window
  ↓ 捕获
document
  ↓
html
  ↓
body
  ↓
目标元素
  ↓ 冒泡
body
  ↓
html
  ↓
document
  ↓
window
```

利用事件冒泡的特点，可以将对子元素的事件处理交由（绑定）到父元素上处理（监听），这就是**事件委托**——利用事件冒泡，把事件监听器绑在父元素上，由父元素统一处理子元素的事件。

需要强调：事件委托**不是新的事件机制**，而是：**事件冒泡的一种应用模式**。

使用事件委托的好处：

+ 减少事件监听器数量（性能好）。子元素若要完成相同或类似的事件处理器，不用单独给每一个子元素添加事件处理器，只用将事件处理器添加到父元素上即可。
+ 支持“动态新增元素”。当使用JavaScript代码动态新增元素时，新元素可以直接应用事件处理器。

在事件委托中还需要关注`Event`对象的这两个属性：**.target**和**.currentTarget**。

+ `event.target`：真正被点击的元素
+ `event.currentTarget`：绑定事件的元素

使用 `event.target` 来获取事件的目标元素（也就是最里面的元素）。如果我们想访问处理这个事件的元素，我们可以使用 `event.currentTarget`。



## DOM（文档对象模型）

Web浏览器的重要部分：

+ 窗口（window）是载入网页的浏览器标签；在 JavaScript 中，它由 `Window`对象表示。使用这个对象上的方法，你可以做一些事情，比如返回窗口的大小（见 `Window.innerWidth` 和 `Window.innerHeight`），操作加载到窗口的文档，在客户端存储该文档的特定数据（例如使用本地数据库或其他存储机制），为当前窗口附加一个事件处理器等。
+ 导航器（navigator）在网络上出现时，代表浏览器的状态和身份（即用户代理）。在 JavaScript 中，它由 `Navigator`对象表示。你可以用这个对象来检索用户的首选语言、用户网络摄像头的媒体流等信息。
+ 文档（document，在浏览器中用 DOM 表示）是加载到窗口的实际页面，在 JavaScript 中，它由 `Document`对象表示。你可以使用这个对象来返回和操作构成文档的 HTML 和 CSS 的信息，例如，在 DOM 中获得一个元素的引用，改变其文本内容，对其应用新的样式，创建新的元素并将其作为子元素添加到当前元素中，甚至完全删除它。

**DOM（Document Object Model，文档对象模型）**是 **浏览器把 HTML / XML 文档抽象成的一棵“可编程的对象树”**，让 **JavaScript 可以读取、修改、删除、创建页面内容和结构**。

需要强调：DOM **不是 JavaScript 标准**；DOM 是 **浏览器实现的 API**；JavaScript 只是**最常用的操作 DOM 的语言**。像`Node.js`默认没有 DOM。



### DOM树

浏览器解析HTML、构建DOM树、提供 API 给 JavaScript操作这棵树。

一个简单的HTML文档：

```html
<html>
  <body>
    <div id="box">Hi</div>
  </body>
</html>
```

对应的 DOM 树（简化）：

```
Document
 └── html
     └── body
         └── div#box
             └── "Hi"
```

DOM 中的一切都是 Node（节点）：

| 类型      | 说明               |
| --------- | ------------------ |
| Element   | 元素节点（div、p） |
| Text      | 文本节点           |
| Attribute | 属性节点           |
| Document  | 整个文档           |

JavaScript操作DOM**通过`document`对象获取DOM树**，然后再使用浏览器DOM提供的API进行编程。



### 操作DOM

***相关API，详见：[文档对象模型（DOM） - Web API | MDN](https://developer.mozilla.org/zh-CN/docs/Web/API/Document_Object_Model)。***



`document`对象是DOM 的入口，是所有节点的根，提供查找、创建、操作节点的方法。

示例：

```js
// 选取文档中的`<a>`标签元素
const link = document.querySelector("a");

// 修改`<a>`标签属性和值
link.href = "https://www.baidu.com";
link.textContent = "百度一下";

const box = document.querySelector("div");
// 创建一个`<p>`标签
const para = document.createElement("p");
para.textContent = "书山有路勤为径，学海无涯苦作舟。";
// 将`<p>`标签追加到`<div>`标签中
box.appendChild(para);
```



#### 选择DOM内的元素（节点）

+ `document.querySelector()`方法。

  `Document.querySelector()`是推荐的现代方法。它很方便，因为它允许你使用 CSS 选择器来选择元素。

+ `document.querySelectorAll()`方法

  想对多个元素进行匹配和操作，可以使用 `Document.querySelectorAll()`，它可以匹配文档中与选择器相匹配的每个元素，并将它们的引用存储在一个叫做 `NodeList` 的类数组对象中。

+ `document.getElementById()`方法

  `Document.getElementById()`，选择一个 `id` 属性值已知的元素，例如 `<p id="myId">My paragraph</p>`。ID 作为参数传递给函数，即 `const elementRef = document.getElementById('myId')`。



#### 创建并放置新的节点

+ `document.createElement()`方法

  `Document.createElement()`可以在DOM中新创建一个元素，但要注意它只是创建出来，还没有添加到DOM中。

+ `node.appendChild()`方法

  `Node.appendChild()`将作为方法参数的元素添加到DOM中，并成为调用该方法的元素的子元素。



#### 删除节点

+ `node.removeChild()`方法

  `Node.removeChild()`删除调用该方法的元素节点的特定子节点（方法参数给出）。

+ `element.remove()`方法

  `Element.remove()`删除调用该防范的元素节点。



#### 操作样式

可以使用 `Document.stylesheets`来获得一个附加在文档上的所有样式表的列表，它返回一个包含 `CSSStyleSheet` 对象的类数组。然后你就可以根据需要添加/删除样式了。



## 发送请求（从服务器获取数据）

### XMLHttpRequest API

在旧的代码中，可能会看到另一个名为 [`XMLHttpRequest`](https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest)（经常会被简写为“XHR”）的 API，它也用于发送 HTTP 请求。其早于 Fetch API，而且是第一个广泛用于实现 AJAX（Asynchronous JavaScript And XML，异步JavaScript和XML） 的 API。

如果可以，建议使用 Fetch：它是一个更简单的 API，而且比 `XMLHttpRequest` 的特性更多。

示例：

```js
const request = new XMLHttpRequest();

try {
  request.open("GET", "url");

  request.responseType = "json";

  request.addEventListener("load", () => initialize(request.response));
  request.addEventListener("error", () => console.error("XHR error"));

  request.send();
} catch (error) {
  console.error(`XHR error ${request.status}`);
}

function initialize(data) {
    let para = document.querySelector("p");
    para.textContent = data.description;
};
```

说明：

1. 创建一个新的 `XMLHttpRequest` 对象。
2. 调用它的 `open()`以进行初始化。
3. 为其添加 `load`事件的事件监听器，其会在响应加载完成时触发。在监听器中，我们调用 `initialize()` 函数。
4. 为其添加 `error` 事件的事件监听器，其会在请求失败时触发。
5. 发送请求。



### Fetch API

 [Fetch API](https://developer.mozilla.org/zh-CN/docs/Web/API/Fetch_API)，它允许页面中运行的 JavaScript 向服务器发起 [HTTP](https://developer.mozilla.org/zh-CN/docs/Web/HTTP) 请求来获取特定的资源。

示例：

```js
// 调用 `fetch()`，传入 URL。
fetch(url)
  // fetch() 返回一个 promise。当我们从服务器收到响应时，
  // 会使用该响应调用 promise 的 `then()` 处理器。
  .then((response) => {
    // 如果请求没有成功，我们的处理器会抛出错误。
    if (!response.ok) {
      throw new Error(`HTTP 错误：${response.status}`);
    }
    // 否则（如果请求成功），我们的处理器通过调用
    // response.json() 以获取json形式的响应，
    // 并立即返回 `response.json()` 返回的 promise。
    return response.json();
  })
  // 若成功调用 response.json()，会使用返回的json来调用 `then()` 处理器，
  // 然后我们将其拷贝到 `para` 段落的内容中。
  .then((json) => (para.textContent = json))
  // 捕获可能出现的任何错误，
  // 并在 `<p>`标签 para段落中显示数据。
  .catch((error) => (para.textContent = `获取数据失败：${error}`));
```



### 其他的网络请求工具（库）

**Axios**（事实上的行业标准）：使用场景：Vue / React / 后台管理系统 / 企业级项目。

特点：

+ 基于 Promise

+ 自动 JSON 转换

+ 拦截器（请求 / 响应）

+ 请求取消

+ 对旧浏览器友好（封装 XHR）

+ 前后端统一接口风格（Node + Browser）



## JSON

### JSON概览

**JavaScript 对象表示法**（JavaScript Object Notation，**JSON**）是一种数据交换格式。虽然它是基于 JavaScript 语法（尽管不是严格意义上的子集，JSON 非常接近 JavaScript 语法的子集），但它独立于 JavaScript，这也是为什么许多程序环境能够读取（解读）和生成 JSON。

JSON 可以表示数字、布尔值、字符串、`null`、数组（值的有序序列），以及由这些值（或其他数组与对象）组成的对象（字符串与值的映射）。JSON 本身不支持复杂的数据类型（函数、正则表达式、日期等）。（日期对象默认会转化为 ISO 格式的字符串，因此信息不会完全丢失。）如果需要 JSON 表示其他数据类型，可在序列化时或反序列化前转换值。

JSON 可以作为一个对象或者字符串存在，前者用于解读 JSON 中的数据，后者用于通过网络传输 JSON 数据。JavaScript 提供一个全局的、可访问的 [JSON](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/JSON) 对象来对这两种数据进行转换。

一个 JSON 对象可以被储存在它自己的文件中，这基本上就是一个文本文件，扩展名为 `.json`

使用`{}`括起来的JSON，构建一个数据层次结构：

```json
{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}
```

把字符串加载到 JavaScript 程序中，并将其解析到一个名为 `obj` 的变量，可以通过点/括号表示法来访问其中的数据，如`obj.numbers[1].powers[0]`

使用`[]`括起来，构成JSON数组：

```json
[
  {
    "name": "Molecule Man",
    "age": 29,
    "secretIdentity": "Dan Jukes",
    "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
  },
  {
    "name": "Madame Uppercut",
    "age": 39,
    "secretIdentity": "Jane Wilson",
    "powers": [
      "Million tonne punch",
      "Damage resistance",
      "Superhuman reflexes"
    ]
  }
]
```

若被JavaScript解析后成为一个变量`obj`，通过数组下标就可以访问，如`obj[0].powers[1]`。



浏览器拥有一个内建的 JSON，包含以下两个方法。

- `parse()`：以文本字符串形式接受 JSON 对象作为参数，并返回相应的对象。
- `stringify()`：接收一个对象作为参数，返回一个对应的 JSON 字符串。



### JSON数据格式

