const fs = require('fs');
const { EOL } = require('os')

const formatContent = (meals) =>{
    let formatString = ''
    for (const meal in meals){
        const mealArr = meals[meal]
        const mealTitle = meal[0].toUpperCase() + meal.slice(1)
        formatString += `*** ${mealTitle} *** ${EOL}`
        mealArr.forEach(m => {formatString += `${m.price} ${m.name} ${m.quantity} ${EOL}`})
    }
    return formatString
}

const main = (csv, cb) => {
    fs.readFile(csv, 'utf8', (err, data) => {
        if (err) {
            return cb(err);
        }
        const meals = {};
        for (const meal of data.split(EOL)) {
            const [mealType, name, quantity, price] = meal.split(',')
            const mealObj = {name: name, quantity: quantity, price: price}
            if (mealType in meals) {
                meals[mealType].push(mealObj)
            }
            else {
                meals[mealType] = [mealObj]
            }
        }
        /*
        let formatString = ''
        for (const meal in meals){
            const mealArr = meals[meal]
            const mealTitle = meal[0].toUpperCase() + meal.slice(1)
            formatString += `*** ${mealTitle} *** ${EOL}`
            mealArr.forEach(m => {formatString += `${m.price} ${m.name} ${m.quantity} ${EOL}`})
        }
        */ //put into new function(meals)
        cb(null, formatContent(meals))
});
}

main('menu.csv', (err, formatContent) => {
    if (err) {console.log(err)}
    else {fs.writeFile('menu.txt', formatContent, (err) => {
        if (err) {console.log(err)}})
}});