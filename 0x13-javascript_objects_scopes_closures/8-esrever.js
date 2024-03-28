#!/usr/bin/node
exports.esrever = function (list) {
  let MyListLength = list.length - 1;
  let myIndx = 0;
  while ((MyListLength - myIndx) > 0) {
    const TempoVar = list[MyListLength];
    list[MyListLength] = list[myIndx];
    list[myIndx] = TempoVar;
    myIndx++;
    MyListLength--;
  }
  return list;
};
