#!/usr/bin/node
// script that reads and prints the content of a file
const fs = require('fs');
const myArgs = process.argv.slice(2);
fs.readFile(myArgs[0], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
