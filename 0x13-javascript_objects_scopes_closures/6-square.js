#!/usr/bin/node
const prevSquare = require('./5-square');
class Square extends prevSquare {
  // Method to print Square instance using given character or 'X'
  charPrint (c = 'X') {
    let row = '';
    let i = 0;
    for (i = 0; i < this.width; i++) {
      row += c;
    }
    for (i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}
module.exports = Square;
