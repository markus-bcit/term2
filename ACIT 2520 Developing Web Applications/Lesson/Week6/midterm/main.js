
const fs = require('fs');
const { EOL } = require('os')

const coffeeArray = { 'DR': 'dark-roast', 'MR': 'medium-roast', 'B': 'blonde' }

const viewAllSupply = (coffeeAbbreviation, cb) => {
    if (!['DR', 'MR', 'B'].includes(coffeeAbbreviation)) {
        cb("Coffee type is not 'DR', 'MR', or 'B'")
    }
    else {
        fs.readFile('supply.txt', 'utf8', (err, data) => {
            if (err) {
                cb(err);
            }
            let coffeeType = coffeeArray[coffeeAbbreviation]
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
}



const addSupply = (coffeeAbbreviation, cb) => {
    if (!['DR', 'MR', 'B'].includes(coffeeAbbreviation)) {
        cb("Coffee type is not 'DR', 'MR', or 'B'")
    }
    else {
        let coffeeType = coffeeArray[coffeeAbbreviation]
        fs.appendFile('supply.txt', `${EOL}${coffeeType}`, (err) => {
            if (err) { cb(err) }
            else { cb(null, "Coffee added successfully") }
        })
    }
}




const deleteSupply = (coffeeAbbreviation, quantity, cb) => {
    if (!['DR', 'MR', 'B'].includes(coffeeAbbreviation)) {
        cb("Coffee type is not 'DR', 'MR', or 'B'")
    }
    else {
        fs.readFile('supply.txt', 'utf8', (err, data) => {
            if (err) {
                cb(err);
            }
            else {
                let coffeeList = data.split(EOL)
                if (quantity === '*') {
                    for (const index in coffeeList) {
                        if (coffeeList[index] === coffeeArray[coffeeAbbreviation]) {
                            coffeeList[index] = ''
                        }
                    }
                }
                if (typeof (quantity) === 'number') {
                    let temp = true
                    let i = 0
                    for (const index in coffeeList) {
                        if (coffeeList[index] === coffeeArray[coffeeAbbreviation]) {
                            coffeeList[index] = ''
                            i++;
                        }
                        if (i === quantity) {
                            break
                        }
                    }

                }
                let formattedCoffee = coffeeList.filter(elm => elm)
                fs.writeFile('supply.txt', formattedCoffee.join(EOL), (err) => {
                    if (err) {
                        cb(err);
                    }
                    else {
                        cb(null, 'Coffee deleted successfully')
                    }
                })

            }
        })
    }
}


viewAllSupply('B', (err, content) => {
    if (err) { console.log(err) }
    else {
        console.log(content)
        addSupply('B', (err, content) => {
            if (err) { console.log(err) }
            else {
                console.log(content)
                viewAllSupply('B', (err, content) => {
                    if (err) { console.log(err) }
                    else {
                        console.log(content)
                        deleteSupply('B', 2, (err, content) => {
                            if (err) { console.log(err) }
                            else {
                                console.log(content)
                                viewAllSupply('B', (err, content) => {
                                    if (err) { console.log(err) }
                                    else {
                                        console.log(content)
                                        console.log('Program is completed')
                                    }
                                })
                            }
                        })
                    }
                })
            }
        })
    }
})