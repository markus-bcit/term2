
//Question1:
// const process = require('process');

// const readAbleStream = process.stdin
// const writeAbleStream = process.stdout

// readAbleStream.pipe(writeAbleStream)

/*
stream that takes some text from terminal 
and write it back to the terminal uppercase
*/

const process = require('process');
const { Transform, pipeline } = require('node:stream');

const rs = process.stdin



const upperCaser = new Transform({
  transform(chunk, encoding, push) {
    push(null, chunk.toString().toUpperCase());
  },
});

const ws = process.stdout

pipeline(rs, upperCaser, ws, (err) => {
    if (err) {console.log(err);}
})





