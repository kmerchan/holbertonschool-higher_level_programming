#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  let i = x;
  for (i = x; i > 0; i--) {
    theFunction();
  }
};
