// script that adds the class red to the HTML header tag
// when the user clicks on the tag DIV#red_header
// using jQuery API
$('DIV#red_header').click(function () {
  $('header').addClass('red');
});
