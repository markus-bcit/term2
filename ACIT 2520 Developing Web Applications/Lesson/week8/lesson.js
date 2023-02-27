// buffer-copy.js
const {
    readFileSync,
    writeFileSync
} = require('fs');

// BUFFER WAY - stores bunch of bytes
const [,, src, dest] = process.argv
const content = readFileSync(src) // reads the entire file into the buffer
writeFileSync(dest, content) // buffer is like an array that sits in computers ram

// STREAM WAY - low memory footprint - allows data to be processed right away
const srcStream = createReadStream(src)
const destStream = createWriteStream(dest)
srcStream.on('data', (data) => destStream.write(data)) // implementation is not optional

//stream and buffers 
// Creates buffer 
const fs = require("fs");
fs.writeFile("myFile.txt", "some content", (err) => {
    if (err) {
        console.log(err);
    } else {
        fs.readFile("myFile.txt", (err, data) => {
            if (err) {
                console.log(err);
            } else {console.log(data);
            }})
    }}) 

/*
            BACKPRESSURE
when writing large amounts of data you should make 
sure that you handle the STOP WRITE EVENT and 
the DRAIN EVENT
*** write = read
*/

src.Stream.on("data", (data) => {
    const canContinue = destStream.write(data);
    if (!canContinue) {
        srcStream.pause
    }})

/*
- Duplex Steam
    - streams that are both readable and writable        
*/