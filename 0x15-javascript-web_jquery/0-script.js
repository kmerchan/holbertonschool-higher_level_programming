#!/usr/bin/node
// script to update the text color of the HTMLtag header to red
const header = document.querySelectorAll('header')
header.forEach(function () {
  style="color: red;"
});
