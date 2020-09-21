#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let occurrence = 0;
  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      occurrence += 1;
    }
  }
  return occurrence;
};
