#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let NumberOfOccurences = 0;
  for (let idx = 0; idx < list.length; idx++) {
    if (searchElement === list[idx]) {
      NumberOfOccurences++;
    }
  }
  return NumberOfOccurrences;
};
