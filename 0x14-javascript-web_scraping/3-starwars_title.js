#!/usr/bin/node
// prints the title of a Star Wars from API.
const request = require('request');

request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    console.log(info.title);
  }
});
