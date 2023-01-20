const math = require("./mathHelpers.js");
const fs = require("fs");

const processInput = (argv) => {
  fs.mkdir("dataPoints", (err) => {
    if (err) {
      console.log(err);
    } else {
      console.log("Folders created successfully");
    }
    fs.writeFile("dataPoints/points.txt", `${argv.slice(2)}`, (err) => {
      if (err) {
        console.log(err);
      } else {
        console.log("File created successfully");
        fs.appendFile(
          "dataPoints/points.txt",
          `
The distance between (${argv[2]}, ${argv[3]}), (${argv[4]}, ${argv[5]}) is ${math.distance(argv[2], argv[3], argv[4], argv[5])}`,
          (err) => {
            if (err) {
              console.log(err);
            } else {
              console.log("Content Saved");
            }
          }
        );
      }
    });
  });
};
processInput(process.argv);
