// 定义变量
let sum = 10000;
// 定义常量
const MAX = 999;
// 修改变量值
sum = 100;
console.log(sum, MAX);
// 修改常量值，会报错。
// MAX = 1000;
// TypeError: Assignment to constant variable.

// 声明变量，但未赋值
let unassigned;
console.log(unassigned);

// 定义函数
function myFunction() {
  console.log("自定义一个函数！");
}

// 调用函数
myFunction();

// 算术运算符
let a = 0,
  b = 0;
a++;
b--;
console.log(a);
console.log(b);
a += 10;
b -= 10;
console.log(a);
console.log(b);
a *= 10;
b /= 10;
console.log(a);
console.log(b);
a %= 13;
console.log(a);
console.log(3 / 5);
console.log(3.64 % 2.5);
console.log("3**5 =", 3 ** 5);

// 字符串拼接
let str1 = "hello ",
  str2 = "world !";
let str3 = str1 + ", Jack.";
console.log(str3);
str1 += str2;
console.log(str1);

// for...of循环
for (let i of [1, 2, 3, 4, 5]) {
  console.log(i);
}
// 等价
const arr = [1, 2, 3, 4, 5];
for (let i of arr) {
  console.log(i);
}

// 变量提升
name = "Jack";
console.log(name);
var name;

// 多次声明相同名称的变量
// let age = 18;
// let age = 19;
var age = 20;
var age = 21;

// Number类型
let num1 = 123;
let num2 = 0.123;
let num3 = 3 + 9;
console.log(num1, num2, num3);
let PI = 3.14159;
console.log(PI.toFixed(3));
console.log(typeof Number("8888"));

// String类型
let str01 = "hello world !";
let str02 = "Have a nice day !";
let strt03 = `This is a dog .`;
console.log(str01, str02, strt03);
// 模板字符串
let str04 = "小明";
let words = `你好，${str04}`;
console.log(words);
let result = `3+5=${3 + 5}`;
console.log(result);
words = `${str01}${str02}`;
console.log(words);
let str05 = "Wow!";
let str06 = "So beautiful!";
// 模板字面量
console.log(`${str05}${str06}`);
// + 运算符拼接
console.log(str05 + str06);
// 多行的模板字面量
let sentence1 = `10月1日，天气晴，气温19摄氏度。
今天我要去天安门看升旗仪式！
……
我今天过得很充实！`;
console.log(sentence1);
// 等效的普通字符串
let sentence2 = "10月1日，天气晴，气温19摄氏度。\n今天我要去天安门看升旗仪式！\n……\n我今天过得很充实！";
console.log(sentence2);
// 字符串包含实际引号
let str07 = 'She said,"This is mine!"'; // 或者用反引号`She said,"This is mine!"`
console.log(str07);
let str08 = 'She said,"This is mine!"';
console.log(str08);
// 数值与字符串相加
let money = 100000000;
let dream = "我的存款为：";
console.log(dream + money + "元");
String(money);
console.log("类型：", typeof money, "值：", money);
// 字符串使用
let str09 = "Apple is a fruit.Maybe also is a mobile phone brand.";
console.log(str09.length); // 字符串长度
console.log(str09[0]);
console.log(str09[52]);
console.log(str09.indexOf("App"));
console.log(str09.indexOf("Macs"));
console.log(str09.slice(0, 5));
console.log(str09.slice(46));
let str10 = str09.slice(0, 5);
console.log(str10.toUpperCase());
console.log(str10.toLowerCase());
console.log(str09.replace("Apple", "Banana"));

// Boolean类型
let bool1 = true;
let bool2 = 6 > 5;
console.log(bool1, bool2);

// Array类型
let arr1 = [1, 2, 3, 4, 5];
let seasons = ["Spring", "Summer", "Autumn", "Winter"];
let arr2 = [1, "hello", true, 0.123, "world !"];
console.log(arr1, seasons, arr2);
console.log(arr1[3]);
console.log(seasons[2]);
console.log(arr2[0]);
console.log(arr2[5]);
console.log(arr2.length);
// 多维数组
let matrix = [
  [1, 2, 5, 8],
  [3, 4, 6, 7],
  [9, 10, 11, 12],
];
console.log(matrix[1][2]);
// 字符串与数组转换
let nameStr = "Jack, Tom, John, Mike";
let nameArr = nameStr.split(",");
console.log(nameArr);
// 数组与字符串转换
let courseArr = ["数学", "英语", "语文"];
let courseStr1 = courseArr.join(",");
console.log(courseStr1);
let courseStr2 = courseArr.toString();
console.log(courseStr2);
// 添加元素
courseArr.push("物理"); // 添加一个元素
let newLength = courseArr.push("地理", "历史", "生物"); //添加多个元素
console.log(courseArr);
console.log(newLength);
newLength = courseArr.unshift("化学", "政治"); // 在数组首部添加多个元素
console.log(courseArr);
console.log(newLength);
// 删除元素
let lastCourse = courseArr.pop(); // 从数组中删除最后一个元素
console.log(lastCourse);
let firstCourse = courseArr.shift();
console.log(courseArr);
console.log(firstCourse);

// Object类型
let car = { name: "Benz", color: "white", price: 1000000 };
console.log(car);
console.log(car.name);
let person = { name: "Jack", age: 18 };
console.log(person.name);
let book = { name: "Python", author: { name: "Mike", birth: "1990-01-01" } };
console.log(book.author.name);

let arg1 = "2";
console.log(typeof arg1);
arg1 = 2;
console.log(typeof arg1);
