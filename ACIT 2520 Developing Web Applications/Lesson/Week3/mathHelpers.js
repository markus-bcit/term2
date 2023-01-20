const sqrt = (number) => {
    return number ** (1/2)
}

const square = (number) => {
    return number*number
}

const distance = (x1, y1, x2, y2) => {
    return sqrt(square(x2 - x1) + square(y2 - y1))
}

module.exports = { distance };