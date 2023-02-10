
const fs = require('fs');
const { EOL } = require('os')

const viewAllSupply = (coffeeType, cb) => {
    fs.readFile('supply.txt', 'utf8', (err, data) => {
        if (err) {
            cb(err);
        }
        let coffeeCount = {}
        for (const type of data.split(EOL)) {
            if (type in coffeeCount)
                coffeeCount[type] += 1
            else {
                coffeeCount[type] = 1
            }
        }
        cb(null, coffeeCount[coffeeType]);
    })
}

const addSupply = (coffeeType, cb) => {
    fs.appendFile('supply.txt', `${EOL}${coffeeType}`, (err) => {
        if (err) { cb(err) }
        else {
            viewAllSupply('blonde', (err, content) => {
                if (err) { console.log(err) }
                else {
                    console.log(content)
                }
            })
        }
    })
}
// add callback to addSupply 


viewAllSupply('blonde', (err, content) => {
    if (err) { console.log(err) }
    else {
        console.log(content)
        addSupply('blonde', (err) => {
            if (err) { console.log(err) }

        })
    }
})
