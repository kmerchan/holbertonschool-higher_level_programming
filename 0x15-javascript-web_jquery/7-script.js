// script that fetches the name from Star Wars API URL
// URL: https://swapi-api.hbtn.io/api/people/5/?format=json
// using jQuery API
const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.getJSON(URL, function (data) {
  const name = data.name;
  $('DIV#character').text(name);
});
