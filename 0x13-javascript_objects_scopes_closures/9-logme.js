#!/usr/bin/node
var numberTimes = 0;
exports.logMe = function (item) {
  const printing = numberTimes + ': ' + item;
  console.log(printing);
  numberTimes += 1;
};
