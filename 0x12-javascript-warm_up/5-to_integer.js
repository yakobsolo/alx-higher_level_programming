#!/usr/bin/node
const num = parseInt(process.argv[2], 10);
if (!num) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(process.argv[2]));
}
