#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method to print the rectangle using 'X'
  print () {
    let row = '';
    let i = 0;
    for (i = 0; i < this.width; i++) {
      row += 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log(row);
    }
  }

  // Method to switch the height and width of a rectangle
  rotate () {
    const holder = this.height;
    this.height = this.width;
    this.width = holder;
  }

  // Method that multiplies the width and height by 2
  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
