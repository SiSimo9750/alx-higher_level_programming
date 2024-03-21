#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (mySQsize) {
    super(mySQsize, mySQsize);
  }
}

module.exports = Square;
