#!/usr/bin/node
// script that counts the number of films Wedge Antilles is in
const request = require('request');
const myArgs = process.argv.slice(2);
let result = 0;
request(myArgs[0], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    let i = 0;
    for (i = 0; i < results.length; i++) {
      let j = 0;
      const character = results[i].characters;
      for (j = 0; j < character.length; j++) {
        if (character[j].includes('18')) {
          result += 1;
        }
      }
    }
    console.log(result);
  }
});
