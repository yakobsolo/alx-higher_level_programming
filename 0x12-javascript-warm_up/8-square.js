#!/usr/bin/node
let i;
const siz = parseInt(process.argv[2]);
if (!siz) {
  console.log('Missing size');
} else {
  for (i = 0; i < siz; i++) {
    console.log('X'.repeat(siz));
  }
}
