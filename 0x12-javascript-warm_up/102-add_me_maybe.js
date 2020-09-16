#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  const i = number + 1;
  theFunction(i);
};
