// script that fetches the value of hello from language API URL
// URL: https://fourtonfish.com/hellosalut/?lang=
// where the language is the value of the tag INPUT#language_code
// using jQuery API
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const URL = 'https://www.fourtonfish.com/hellosalut/?lang=';
    const urlLang = URL + $('INPUT#language_code').val();
    $.getJSON(urlLang, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
