// Importing node.js modules
const os = require('os');
console.log(os.freemem());

//Function declaration syntax
greet('Markus');
//can call function before function is defined, because js has a mechanism called hoisting,
// so before code is run, it scans for functions, and pulls it to the top of the file *behind the scenes*,
// this isn't beneficial 100% of the time.
function greet(name){
    `Hello ${name}, how are you`;
}

// Function Expression Syntax
//^^THESE TYPES OF FUNCTIONS DO NOT HOIST^^, main purpose of this type of function
const greet = function (name){
    console.log(`Hello ${name}, how are you`);
}

// Arrow function syntax *no hoisting as well*
// 'const' and 'let' is not required in functions, but can turn local variables into global variables, which can be bad!!
const greet = (firstName) => {
    console.log(`Hello ${firstName}, how are you`)
}
// OR (to make more simpler)
const greet = (firstName) => `Hi ${firstName}`;

//OR
const greet2 = firstName => {
    const greeting = `Hi ${firstName}`;
    return greeting;
}

// always use const except in cases where you cant use const
const colors = ['red', 'blue']
//can modify a const, but can't reassign a const variable
colors.push('green')
colors = ['blue', 'red'] //<---- THIS WOULD NOT WORK
//why you shouldn't use var; as if you try to call a var before assigning
//it will give undefined instead of an error, var has hoisting, but it only hoist the variable and not the value assigned to the variable,
//which is why its undefined.
console.log(firstName)
var firstName = 'john';

//assigning variables to var, will not have them as block-scoped variable, even if in a for loop, or if statement,
//only time it will be block-scoped, is in a function.
if (true) {
    var abc = 'abc' //<----- not block-scoped, global variable.
}

//better to use let, as the variable will stay local to the block-scope
for (let i = 0; i < 10; i++){
}
function add(num1, num2) {
    return num1 + num2;
}

add(4, 3);

We can also invoke the add function

indirectly

const referenceOne = add
referenceOne(3, 7)
const referenceTwo = add;
referenceTwo(9, 8)

function addTwo(num1, addreference) {
    return addreference(num1, 2);
}

console.log(addTwo(7, add))
//^^^ call back function ^^^

for loops
for (let i = 0; i < 10; i++) {
}
for (const key in object){
}

const colors = ["red", "green", "blue"]

function forEach(list,cb) {
    for (let i of list) {
        cb(i);
    }
}

function callback(value) {
    console.log(value)
}

forEach(colors,callback);

// lil activity

const multiplier = (n1, n2, callback) => {
    if ((typeof(n1) !== 'number') || (typeof(n2) !== 'number')) {
        callback(new Error("Error: Invalid"));
    }
    else {callback(null, parseInt(n1 * n2));}
}

const cb = (err, result) => {
    if (err) {
        console.log(result);
    }
    else {
        console.log(result);
    }
}

multiplier(5, 4, cb)

^^ cb can be added straight into multiplier function

multiplier(5, 4, (err, result) => {
    if (err) {
        console.log(result);
    }
    else {
        console.log(result);
    })

const fs = require("fs");

fs.writeFile("amazon.txt", "This is amazon", (err, data) => {
  if (err) {
    console.log(data);
  }
});
// ^^^^creates file ^^^

const content = fs.readFileSync("cit.txt", "utf8");
// ^^^ 'Sync' must read the entire file before going to the next
console.log(content);

const content = fs.readFile("cit.txt", "utf8");

fs.readFile("cit.txt", "utf8", (err, data) => {
  if (err) {
    console.log(data);
  } else {
    console.log(data);
  }
});

// unsafe if file is being made then the file cant be read so::

fs.writeFile("amazon.txt", "This is amazon", (err, data) => {
  if (err) {
    console.log(data);
  }
  fs.readFile("cit.txt", "utf8", (err, data) => {
    if (err) {
      console.log(data);
    } else {
      console.log(data);
    }
  });
});
