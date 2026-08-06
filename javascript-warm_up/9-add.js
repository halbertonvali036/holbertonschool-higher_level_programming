#!/usr/bin/node
function add (a, b) {
  return a + b;
}

const firstArg = parseInt(process.argv[2], 10);
const secondArg = process.argv[3];
const secondNum = parseInt(secondArg, 10);

if (process.argv.length < 4 && secondArg === undefined) {
  console.log(NaN);
} else {
  console.log(add(firstArg, secondNum));
}
