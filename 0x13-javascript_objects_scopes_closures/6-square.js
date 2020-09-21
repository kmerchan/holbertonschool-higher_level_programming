#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
