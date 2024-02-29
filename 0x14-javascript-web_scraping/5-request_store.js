#!/usr/bin/node
//  gets the contents of a webpage and stores it in a file.
const request = require('request');
const fs = require('node:fs');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(process.argv[3], body, (err) => {});
});
