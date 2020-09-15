#!/usr/bin/node
const myArgs = process.argv.splice(2);
const num1 = Number(myArgs[0]);
function factorial (num) {
  if (isNaN(num) || num < 1) {
    return (1);
  }
  return (num * factorial(num - 1));
}
console.log(factorial(num1));
