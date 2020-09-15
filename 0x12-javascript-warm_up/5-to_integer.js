#!/usr/bin/node
const myArgs = process.argv.slice(2);
const num = Number(myArgs[0]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
