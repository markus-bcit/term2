// const os = require('os');
// console.log(os.cpus().length);

const { time, Console } = require("console");


// console.log(process.argv[2], process.argv[3])



const wordPosition = (words) => {
    let word_obj = {}
    for (let i = 0; i < words.length; i++) {
        if (word_obj[i] of words) {
            word_obj.push(words[i])
        } else {
            word_obj[i] = i
        }
    }
    console.log(word_obj)
    // let word_obj = {}
    // for (let i = 0; i < words.length; i++) {
    //     let item = words[i];
    //     if (item in word_obj) {
    //         word_obj[item].push(i)
    //     } else {
    //         word_obj[item] = [i]
    //     }
    // }
    // console.log(word_obj)
}


    
    const input = [
      "buy",
      "it",
      "use",
      "it",
      "break",
      "it",
      "fix",
      "it",
      "trash",
      "it",
      "change",
      "it",
      "mail",
      "upgrade",
      "it",
    ];
    
   wordPosition(input);
    
    /*
    Output should look like so:
    {
      break: [ 4 ],
      buy: [ 0 ],
      change: [10],
      fix: [ 6 ],
      it:  [1, 3, 5, 7, 9, 11, 14],
      mail: [ 12 ],
      trash: [ 8 ],
      upgrade: [ 13 ],
      use: [ 2 ],
    }
    
    */