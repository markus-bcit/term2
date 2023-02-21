// // // // const fs = require("fs");
// // // // fs.writeFile("myFile.txt", "some content", (err) => {
// // // //     if (err) {
// // // //         console.log(err);
// // // //     } else {
// // // //         fs.readFile("myFile.txt", (err, data) => {
// // // //             if (err) {
// // // //                 console.log(err);
// // // //             } else {console.log(data);
// // // //             }})
// // // //     }

// // // // }
// // // // )

// // // // const { argv } = require("process");
// // // // const x1 = argv[0]; // "10"
// // // // const y1 = argv[1]; // "5"
// // // // const x2 = argv[2]; // "2" 
// // // // const y2 = argv[3]; // "3"
// // // // console.log(x1, y1, x2)



// // // const fs = require("fs");
// // // fs.readFile("file1.txt", "utf8", (err, fileTwo) => {
// // //     if (err) {
// // //     }
// // //     console.log(err);
// // //     fs.readFile(fileTwo, "utf8", (err, fileThree) => {
// // //         if (err) {
// // //         }
// // //         console.log(err);
// // //         fs.readFile(fileThree, "utf8", (err, fileFour) => {
// // //             if (err) {
// // //             }
// // //             console.log(err);
// // //             fs.readFile(fileFour, "utf8", (err, fileFourResult) => {
// // //                 if (err) {
// // //                 }
// // //                 console.log(err);
// // //                 console.log('Contents of file4: ${fileFourResult}');
// // // })
// // //         })
// // //     })
// // // })


// // function powerOf(number1, number2, callback) {
// //     if (typeof number1 !== 'number' || typeof number2 !== 'number') { callback(new Error('the first and second arguments must be number')); } else {
    
// //     const result = Math.pow(number1, number2);
// //     callback(null, result);}
// // }
// // powerOf(3, 4, function (err, result) {
// //     if (err) {
// //         console.log(err);
// //     } else {
// //         console.log(result);
// //     }
// // });


// let squareRoot = num => {return Math.sqrt(num)};
// let square = num => {return num * num};
// module.exports =
// {squareRoot, square };

// let squareRoot = num => return Math.sqrt(num);

// let square = num => return num * num;

const coffeeArray = {'DR': 'dark-roast', 'MR': 'medium-roast' , 'B': 'blonde'}

console.log(coffeeArray['MR'])