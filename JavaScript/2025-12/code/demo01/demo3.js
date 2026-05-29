let obj1 = {};
console.log(typeof obj1);
console.log(obj1);

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

// 书对象
let book = {
  name: "JavaScript",
  price: 48.8,
  printInfo() {
    console.log(`Book name is ${this.name}`);
  },
};
book.printInfo();
// 设置和添加成员
book.name = "New JavaScript";
book["price"] = 66.2;
book.author = "John";
book.printInfo = function () {
  console.log(`Book name is ${this.name}, and price is ${this.price}.`);
};
console.log(book);
book.printInfo();
// 动态添加成员
let propertyName = "publication";
let propertyValue = "2022-06-08";
book[propertyName] = propertyValue;
console.log(book);

// 创建对象，通过函数
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
console.log(book1);
book1.printInfo();
console.log(book2);
book2.printInfo();

// 创建对象，通过构造函数
function Book(name, price) {
  this.name = name;
  this.price = price;
  this.printInfo = function () {
    console.log(`Book name is ${this.name}, and price is ${this.price}.`);
  };
}
let book3 = new Book("Java", 39.8);
let book4 = new Book("C++", 48.8);
console.log(book3);
book3.printInfo();
console.log(book4);
book4.printInfo();
