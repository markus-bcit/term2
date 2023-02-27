const { Transform } = require('stream');


let profit = 0
const sumProfit = () => {
    return new Transform({
        transform: function (chunk, enc, push) {
            const obj = JSON.parse(chunk)
            profit += parseFloat(obj.profit)
            push(null)
        },
        flush: function (push) {
            push(null, "$" + profit)
        }
    })
}

module.exports = { sumProfit };