#!/usr/bin/node
const myVar = 'C is fun';
const myArgs = process.argv.splice(2);
const num = Number(myArgs[0]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  for (i = 0; i < num; i++) {
    console.log(myVar);
  }
}
