#!/usr/bin/node
const numr = parseInt(process.argv[2]);
function factorial (numr) {
  if (!numr || numr === 0) {
    return (1);
  } else {
    return (numr * factorial(numr - 1));
  }
}
console.log(factorial(numr));
