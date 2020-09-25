// script that fetches the value of hello from French API URL
// URL: https://fourtonfish.com/hellosalut/?lang=fr
// using jQuery API
$(document).ready(function () {
  const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.getJSON(URL, function (data) {
    const hello = data.hello;
    $('DIV#hello').text(hello);
  });
});
