#!/usr/bin/node
function add (a, b) {
  const mySum = a + b;
  console.log(mySum);
}

add(Number(process.argv[2]), Number(process.argv[3]));
