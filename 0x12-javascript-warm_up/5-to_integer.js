#!/usr/bin/node
const MyNumber = Math.floor(Number(process.argv[2]));
console.log(isNaN(MyNumber) ? 'Not a number' : `My number: ${num}`);
