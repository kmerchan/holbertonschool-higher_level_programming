#!/usr/bin/node
const myArgs = process.argv.splice(2);
if (myArgs.length === 0 || myArgs.length === 1) {
  console.log(0);
} else {
  let i = 0;
  let max = 0;
  let result = 0;
  if (Number(myArgs[0]) > Number(myArgs[1])) {
    max = myArgs[0];
    result = myArgs[1];
  } else {
    max = myArgs[1];
    result = myArgs[0];
  }
  for (i = 2; i < myArgs.length; i++) {
    if (Number(myArgs[i]) >= Number(max)) {
      result = max;
      max = myArgs[i];
    } else if (Number(myArgs[i]) >= Number(result)) {
      result = myArgs[i];
    }
  }
  console.log(result);
}
