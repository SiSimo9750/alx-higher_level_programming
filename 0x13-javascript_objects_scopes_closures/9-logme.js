#!/usr/bin/node
let myArgument = 0;

exports.logMe = function (item) {
  console.log(myArgument + ': ' + item);
  myArgument++;
};
