#!/usr/bin/node
const myArgs = process.argv.splice(2);
const num1 = Number(myArgs[0]);
const num2 = Number(myArgs[1]);
function add (a, b) {
  return (a + b);
}
console.log(add(num1, num2));
