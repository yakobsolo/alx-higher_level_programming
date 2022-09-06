#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];
const sum = parseInt(a) + parseInt(b);
function add (a, b) {
  if (!a || !b) {
    console.log('NaN');
  } else {
    console.log(sum);
  }
}
add(a, b);
