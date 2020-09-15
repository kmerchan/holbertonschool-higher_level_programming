#!/usr/bin/node
const myVar = 'X';
const myArgs = process.argv.splice(2);
const num = Number(myArgs[0]);
if (isNaN(num)) {
  console.log('Missing size');
} else {
  let i = 0;
  let myString = '';
  for (i = 0; i < num; i++) {
    myString += myVar;
  }
  for (i = 0; i < num; i++) {
    console.log(myString);
  }
}
