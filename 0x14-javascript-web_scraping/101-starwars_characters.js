#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const request = require('request');
const myArgs = process.argv.slice(2);
const URLstring = 'https://swapi-api.hbtn.io/api/films/' + myArgs[0];
function characterFunc (character, i = 0, stop) {
  if (i === stop) {
    return;
  }
  const URLcharacter = character[i];
  request(URLcharacter, function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
    }
  });
  i++;
  characterFunc(character, i, stop);
}
request(URLstring, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const character = JSON.parse(body).characters;
    characterFunc(character, 0, character.length);
  }
});
