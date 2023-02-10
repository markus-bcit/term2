const fs = require("fs");
const { EOL } = require("os");

const formatContent = (meals) => {
    let formattedContent = "";
    for (const key in meals) {
        const mealList = meals[key]; // [{name: "sth", quantity: "", price: ""}, {}]
        const uppercaseMealName = key[0].toUpperCase() + key.slice(1);
        formattedContent += `****${uppercaseMealName} items***${EOL}`;
        mealList.forEach(m => formattedContent += `${m.price} ${m.name} ${m.quantity}${EOL}`);
    }
    return formattedContent;
}

const processInputPromise = (csv) => {
    return new Promise((resolve, reject) => {
        fs.readFile(csv, "utf8", (err, data) => {
            if (err) {
                reject(err);
            }
            else {
                const meals = {}; // Dictionary for grouping meals
                for (const meal of data.split(EOL)) {
                    const [mealType, name, quantity, price] = meal.split(",");
                    const mealObj = { name, quantity, price };
                    if (mealType in meals) {
                        meals[mealType].push(mealObj);
                    } else {
                        meals[mealType] = [mealObj]; // [].push(mealObj);
                    }
                }
                resolve(meals)
            }
        });
    });
}
const writeFilePromise = (err, data) => {
    return new Promise((resolve, reject) => {
        if (err) {reject(err)}
        else {fs.writeFile("menu.txt", formatContent(data))
    resolve('File saved')}})
}
processInputPromise("menu.csv").then(meals => {
    fs.writeFile("menu.txt", formatContent(meals), (err) => {
    if (err) { return console.log(err); }
    console.log("File saved")});
});
processInputPromise("menu.csv").catch(err => {
    console.log(err)
})
// processInput("menu.csv", (err, fc) => {
//     if (err) { return console.log(err); }
//     fs.writeFile("menu.txt", fc, (err) => {
//     if (err) { return console.log(err); }
//     console.log("File saved");
//     });
//   });
// processInput("menu.csv", (err, fc) => {
//     if (err) { return console.log(err); }
//     fs.writeFile("menu.txt", fc, (err) => {
//         if (err) { return console.log(err); }
//         console.log("File saved");
//     });
// });



// const new_promise = new Promise((resolve, reject) => {
//     // do something
//     if (err) { return reject(err); }
//     else { resolve(data); }
// }
// new_promise.then(data) => { //do something with data}
// new_promise.catch((err) => {//do something cause err}