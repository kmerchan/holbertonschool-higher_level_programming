#!/usr/bin/node
const myArgs = process.argv.splice(2);
const num1 = Number(myArgs[0]);
function factorial (num) {
  let result = 1;
  let i = 0;
  for (i = num; i > 0; i--) {
    result *= i;
  }
  return result;
}
console.log(factorial(num1));
