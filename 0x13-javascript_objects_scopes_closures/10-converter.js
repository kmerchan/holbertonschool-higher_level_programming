#!/usr/bin/node
exports.converter = function (base) {
  return function innerFunction (inner) {
    return parseInt(inner).toString(base);
  };
};
