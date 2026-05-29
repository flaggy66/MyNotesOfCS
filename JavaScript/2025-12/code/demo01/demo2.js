function myFunction() {
  console.log("自定义了一个函数！");
}

myFunction();
printInfo("李伟", 20, "北京大学");
console.log("默认参数----------");
printInfoByDefault("李伟", 22);
printInfoByDefault("李伟");

function printInfo(name, age, school) {
  console.log("你的名字是：", name);
  console.log("你的年龄是：", age);
  console.log("你的学校是：", school);
}

// 默认参数
function printInfoByDefault(name, age = 18, school = "未知") {
  console.log("你的名字是：", name);
  console.log("你的年龄是：", age);
  console.log("你的学校是：", school);
}

// 匿名函数
(function () {
  console.log("匿名函数");
})();

// 箭头函数
(() => {
  console.log("箭头函数");
})();

alert("hello world");
