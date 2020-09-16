#!/usr/bin/node
const myArgs = process.argv.splice(2);
if (myArgs.length === 0 || myArgs.length === 1) {
  console.log(0);
} else {
  let i = 0;
  let max = 0;
  let result = 0;
  if (Number(myArgs[0]) > Number(myArgs[1])) {
    max = Number(myArgs[0]);
    result = Number(myArgs[1]);
  } else {
    max = Number(myArgs[1]);
    result = Number(myArgs[0]);
  }
  for (i = 2; i < myArgs.length; i++) {
    if (Number(myArgs[i]) > max) {
      result = max;
      max = Number(myArgs[i]);
    }
  }
  console.log(result);
}
