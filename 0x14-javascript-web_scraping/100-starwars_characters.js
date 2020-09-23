#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const request = require('request');
const myArgs = process.argv.slice(2);
const URLstring = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];
request(URLstring, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const character = JSON.parse(body).characters;
    let i = 0;
    for (i = 0; i < character.length; i++) {
      const URLcharacter = character[i];
      request(URLcharacter, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
