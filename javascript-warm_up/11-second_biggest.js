#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2).map(Number);

  let biggest = numbers[0];
  let second = numbers[0];

  for (const num of numbers) {
    if (num > biggest) {
      second = biggest;
      biggest = num;
    } else if (num > second && num !== biggest) {
      second = num;
    }
  }

  console.log(second);
}
