#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((h > 0) && (w > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let idxH = 0; idxH < this.height; idxH++) {
      let Xchar = '';
      for (let idxW = 0; idxW < this.width; idxW++) {
        Xchar += 'X';
      }
      console.log(Xchar);
    }
  }
}

module.exports = Rectangle;
