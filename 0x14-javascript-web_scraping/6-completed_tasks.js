#!/usr/bin/node
// script that computes the number of tasks completed by user id
const request = require('request');
const myArgs = process.argv.slice(2);
request(myArgs[0], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    
  }
});
