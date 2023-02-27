const { createReadStream } = require('fs');
const { filterByCountry } = require('./filter-by-country.js');
const csv = require("csvtojson");
const { sumProfit } = require('./sum-profit.js');
const { createGunzip } = require('zlib');

const csvParser = csv()
const unzipStream = createGunzip()


// first unzip the gzip
createReadStream('data.csv.gz')
  .pipe(unzipStream)
  .pipe(csvParser)
  .pipe(filterByCountry('Italy'))        // (3)
  // .on('data', (chunk) => {console.log(JSON.parse(chunk))})
  .pipe(sumProfit())                     // (4)
  .pipe(process.stdout) 