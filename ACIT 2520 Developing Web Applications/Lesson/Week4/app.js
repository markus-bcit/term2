const fs = require("fs");

// // this was only used to create a dir to test 
// const createfiles = () => {
//     fs.mkdir("files", (err) => {
//         if (err) {
//             console.log(err);
//         } else {
//             console.log("Folders created successfully");
//         }
//         fs.writeFile("files/file4.exe", 'hi', (err) => {
//             if (err) {
//                 console.log(err);
//             } else {
//                 console.log("File created successfully");
//             }
//         })
//     })
// }
// // createfiles()


// // const dir_list = {}
// const callback = (err, list) => {
//     if (err) {
//         console.log(err);
//     } else {
//         console.log(list);;
//     }
    
// }
// const processdir = (argv) => {
//     console.log(fs.readdir(argv[1], callback(err, dir_list)));
// }

// processdir(process.argv)

const files = fs.readdir('files', (err) => {
            if (err) {
                console.log(err);
            } else {
                console.log("Folders created successfully");
            }})

// for (const file of files)
  console.log(files);
