/*
 * Project: Milestone 1
 * File Name: IOhandler.js
 * Description: Collection of functions for files input/output related operations
 *
 * Created Date: February 28, 2023
 * Author: Markus Afonso
 *
 */

const unzipper = require("unzipper"),
  fs = require("fs"),
  PNG = require("pngjs").PNG,
  path = require("path");

/**
 * Description: decompress file from given pathIn, write to given pathOut
 *
 * @param {string} pathIn
 * @param {string} pathOut
 * @return {promise}
 */
const unzip = (pathIn, pathOut) => {
  return new Promise((resolve, reject) => {
    fs.createReadStream(pathIn)
      .pipe(unzipper.Extract({ path: pathOut }))
      .on("error", (error) => {
        reject(`Failed to unzip ${pathIn}: ${error.message}`);
      })
      .on("close", () => {
        resolve(`Files extracted to: ${pathOut}`);
      });
  });
};

/**
 * Description: read all the png files from given directory and return Promise containing array of each png file path
*
* @param {string} path
* @return {promise}
*/
const readDir = (dir) => {
  return new Promise((resolve, reject) => {
    fs.readdir(dir, (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data.filter((file) => file.match(/\.png$/)));
      }
    });
  });
  /*
  return new Promise((resolve, reject) => {
    fs.readdir(dir, (err, files) => {
      if (err) {
        reject(err);
      } else {
        const pngFiles = files.filter((file) => path.extname(file) === ".png")
        const promises = pngFiles.map((file) => {
          return new Promise((resolve) => {
            const pathPngFiles = path.join(__dirname, file)
            resolve(pathPngFiles);
          })
        })
        Promise.all(promises)
        .then((results) => {
          resolve(results);
        })
        .catch((error) => {
          reject(error);
        });
      }
    })
  })
  */
};



/**
 * Description: Read in png file by given pathIn,
 * convert to grayscale and write to given pathOut
*
* @param {string} filePath
* @param {string} pathProcessed
* @return {promise}
*/
const grayScale = (dirIn, dirOut) => {
  return new Promise((resolve, reject) => {
    fs.readdir(dirIn, (err, files) => {
      if (err) {
        reject(err);
      } else {
        const pngFiles = files.filter((file) => path.extname(file) === ".png");
        const promises = pngFiles.map((file) => {
          const pathInFile = path.join(dirIn, file);
          const pathOutFile = path.join(dirOut, file);
          return new Promise((resolve, reject) => {
            fs.createReadStream(pathInFile)
              .pipe(
                new PNG({
                  filterType: 4,
                })
              )
              .on("parsed", function () {
                for (let y = 0; y < this.height; y++) {
                  for (let x = 0; x < this.width; x++) {
                    const idx = (this.width * y + x) << 2;

                    // gray scale
                    this.data[idx] = (this.data[idx] + this.data[idx + 1] + this.data[idx + 2]) / 3;
                    this.data[idx + 1] = (this.data[idx] + this.data[idx + 1] + this.data[idx + 2]) / 3;
                    this.data[idx + 2] = (this.data[idx] + this.data[idx + 1] + this.data[idx + 2]) / 3;
                  }
                }
                this.pack()
                  .pipe(fs.createWriteStream(pathOutFile))
                  .on("error", (error) => {
                    reject(`Failed: ${error.message}`);
                  })
                  .on("close", () => {
                    resolve(`File saved to ${pathOutFile}`);
                  });
              });
          });
        });

        // Wait for all promises to complete
        Promise.all(promises)
          .then((results) => {
            resolve(results);
          })
          .catch((error) => {
            reject(error);
          });
      }
    });
  });
};


module.exports = {
  unzip,
  readDir,
  grayScale,
};
