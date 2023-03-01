const path = require("path");
/*
 * Project: Milestone 1
 * File Name: main.js
 * Description:
 *
 * Created Date: February 28, 2023
 * Author: Markus Afonso
 *
 */

const IOhandler = require("./IOhandler");
const zipFilePath = path.join(__dirname, "myfile.zip");
const pathUnzipped = path.join(__dirname, "unzipped");
const pathProcessed = path.join(__dirname, "grayscaled");

IOhandler.unzip(zipFilePath, pathUnzipped)
	.then((message) => {
		console.log(message);
		return IOhandler.readDir(pathUnzipped);
	})
	.then((message) => {
		console.log(message);
		return IOhandler.grayScale(pathUnzipped, pathProcessed);
	})
	.then((message) => {
		console.log(message);
	})
	.catch((error) => {
		console.error(error);
	});


