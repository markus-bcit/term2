const { Transform } = require('stream');

const filterByCountry = (country) => {
  return new Transform({
    transform: function(chunk, enc, push) {
      const obj = JSON.parse(chunk);
      if (obj.country === country) {
        push(null, chunk)}
      else{
        push(null,null)
      }
    }
  })
}


module.exports = { filterByCountry };