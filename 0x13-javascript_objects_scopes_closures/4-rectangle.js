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

  rotate () {
    const TempoVar = this.width;
    this.width = this.height;
    this.height = TempoVar;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
