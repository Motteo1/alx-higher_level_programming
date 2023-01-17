#!/usr/bin/node

const episodeNum = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
const request = require('request');

request(url + episodeNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error Code: ' + response.statusCode);
  }
});
