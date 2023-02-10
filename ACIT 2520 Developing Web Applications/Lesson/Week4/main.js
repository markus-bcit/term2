const filesearch = require('./app.js')

filesearch.printfiles(process.argv[2], process.argv[3], (err) => {
    if (err) {
        console.error(err)}})