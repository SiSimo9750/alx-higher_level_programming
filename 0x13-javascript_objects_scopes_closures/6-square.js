#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let idxH = 0; idxH < this.height; idxH++) {
      let Cchar = '';
      for (let idxW = 0; idxW < this.width; idxW++) {
        Cchar += c;
      }
      console.log(Cchar);
    }
  }
}

module.exports = Square;
