#!/usr/bin/node
exports.esrever = function (list) {
  const listBackup = list.slice();
  let i = 0;
  for (i = 0; i < list.length; i++) {
    list[i] = listBackup[list.length - i - 1];
  }
  return list;
};
