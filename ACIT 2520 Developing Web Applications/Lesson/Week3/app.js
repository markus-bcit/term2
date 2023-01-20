// const os = require('os');
// os.cpus();
// // purple block => call with ()
// // blue block => no ()

// // File system Module
// const fs = require('fs');


// // Asynchronous 
// fs.writeFile('cit.txt', 'hi', (err) => {
//     if (err) { console.error(err) }
//     //here
// })
// // ^^ move to {here} so the file is made before the file is read
// fs.readFile('cit.txt', { "encoding": "utf-8" }, (err, data) => {
//     if (err) { console.error(err); 
//     } else {console.log(data)
//     }
// })
// // ^^^Windows handles the function and runs the rest of the code^^^

// // 

// function displays(data) {
//     console.log(data)
// }

// const tweet = fetchSync('https://twitter.com/bcit/tweets/1')

// displays(tweet)

// setTimeout(somefuntion, 1000)
// // ^^^waits for timer to run function - timerAPI

// function printHi(){
//     console.log("Hi")
// }

// function blockForOneSec(){
//     console.log("smt")
// }

// setTimeout(printHi, 0)
// blockForOneSec()
// console.log('First')

// // OUTPUT:
// // smt 
// // First
// // Hi => callback queue hold the setTimeout function until everything is executed to start the countdown it is the last to execute 
// //      Note: js only uses a single thread so it sucks at CPU intensive tasks 

// // if function has sync => probs asynchronous asdf


function func2(num) { return num > 2
}
let numberArr = [1, 2, 3, 4];
let greaterThanTwo = numberArr.filter(func2);

console.log(greaterThanTwo)