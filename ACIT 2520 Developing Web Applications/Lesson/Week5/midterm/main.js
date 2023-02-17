
const fs = require('fs');
const { EOL } = require('os')

const viewAllSupply = (coffeeType, cb) => {
    if (!['dark-roast', 'medium-roast', 'blonde'].includes(coffeeType)){
        cb("Coffee type is not 'dark-roast', 'medium-roast', or 'blonde'")
    }
    else{
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
    })}
}

const addSupply = (coffeeType, cb) => {
    if (!['dark-roast', 'medium-roast', 'blonde'].includes(coffeeType)){
        cb("Coffee type is not 'dark-roast', 'medium-roast', or 'blonde'")
    }
    else{
    fs.appendFile('supply.txt', `${EOL}${coffeeType}`, (err) => {
        if (err) { cb(err) }
        else {
            viewAllSupply(coffeeType, (err, content) => {
                if (err) { console.log(err) }
                else {
                    console.log(content)
                    cb(null)
                }
            })
        }
    })}
}

viewAllSupply('blonde', (err, content) => {
    if (err) { console.log(err) }
    else {
        console.log(content)
        addSupply('blonde', (err) => {
            if (err) { console.log(err) }
            else {console.log('Program is Completed')}
        })
    }
})
