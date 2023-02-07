// const fs = require("fs");

// // // this was only used to create a dir to test 
// // const createfiles = () => {
// //     fs.mkdir("files", (err) => {
// //         if (err) {
// //             console.log(err);
// //         } else {
// //             console.log("Folders created successfully");
// //         }
// //         fs.writeFile("files/file4.exe", 'hi', (err) => {
// //             if (err) {
// //                 console.log(err);
// //             } else {
// //                 console.log("File created successfully");
// //             }
// //         })
// //     })
// // }
// // // createfiles()


const fs = require('fs');
const path = require('path');

const directory = process.argv[2];
const extension = process.argv[3];

const callback = (err, files) => {
    if (err) {
        return console.log(err)
    }
    for (file of files) {
        if (path.extname(file) === `.${extension}`){
            console.log(file)
        }
    }}

const printfiles = (directory) => {fs.readdir(directory, callback)}
printfiles(directory)
module.exports = {printfiles};