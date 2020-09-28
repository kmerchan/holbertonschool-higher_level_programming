// script to update the text color of the HTMLtag header to red
// using document.querySelector after document is loaded
document.addEventListener("DOMContentLoaded", function () {
  const header = document.querySelector('header');
  header.style = 'color: red;';
});
